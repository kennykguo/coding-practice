"""Independent cycle models for the refresher's small RTL examples."""
import os
import random
from collections import deque
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles, FallingEdge, RisingEdge, ReadOnly, Timer

RNG = random.Random(426)

async def edge(dut, **values):
    await FallingEdge(dut.clk)
    for name, value in values.items():
        getattr(dut, name).value = value
    await RisingEdge(dut.clk)
    await ReadOnly()

async def reset(dut):
    await edge(dut, rst=1)
    await edge(dut, rst=0)

async def check_counter(dut):
    limit = int(os.environ["LIMIT"])
    count = 0
    for cycle in range(220):
        en, rst = RNG.randrange(2), int(cycle in (60, 149))
        tick = int(not rst and en and count == limit - 1)
        count = 0 if rst else (count + en) % limit
        await edge(dut, en=en, rst=rst)
        assert int(dut.count.value) == count
        assert int(dut.tick.value) == tick

async def check_stream(dut):
    model = deque()
    pending, sent, received, discarded = None, 0, 0, 0
    stalled = None
    for cycle in range(700):
        await FallingEdge(dut.clk)
        rst = cycle in (63, 177)
        if pending is None and sent < 180 and RNG.random() < 0.8:
            pending = (37 * sent + 5) & 255
        ready = int(cycle > 12 and (cycle % 47 > 8) and RNG.random() < 0.65)
        if sent == 180:
            ready = 1
        dut.rst.value = int(rst)
        dut.in_valid.value = int(pending is not None)
        dut.in_data.value = pending or 0
        dut.out_ready.value = ready
        await ReadOnly()
        valid = int(dut.out_valid.value)
        if stalled is not None and not rst:
            assert valid and int(dut.out_data.value) == stalled
        if rst:
            discarded += len(model)
            model.clear()
            stalled = None
        else:
            if valid and ready:
                assert model
                assert int(dut.out_data.value) == model.popleft()
                received += 1
            stalled = int(dut.out_data.value) if valid and not ready else None
            if pending is not None and int(dut.in_ready.value):
                model.append(pending)
                pending = None
                sent += 1
        await RisingEdge(dut.clk)
        await ReadOnly()
        assert int(dut.out_valid.value) == bool(model)
        if model:
            assert int(dut.out_data.value) == model[0]
        if sent == 180 and not model:
            assert received + discarded == sent
            return
    assert False, "Stream did not drain"

async def check_ram(dut):
    mem = {}
    for addr in range(8):
        value = addr * 23
        await edge(dut, wr_en=1, wr_addr=addr, wr_data=value, rd_en=0)
        mem[addr] = value
    for cycle in range(220):
        rd, wr = RNG.randrange(2), RNG.randrange(2)
        ra, wa = RNG.randrange(8), RNG.randrange(8)
        if cycle % 5 == 0:
            rd = wr = 1
            wa = ra
        data, rst = RNG.randrange(256), int(cycle == 100)
        expected = mem[ra]
        await edge(dut, rd_en=rd, wr_en=wr, rd_addr=ra, wr_addr=wa,
                   wr_data=data, rst=rst)
        assert int(dut.rd_valid.value) == bool(rd and not rst)
        if rd and not rst:
            assert int(dut.rd_data.value) == expected
        if wr and not rst:
            mem[wa] = data

async def check_mac(dut):
    for cycle in range(260):
        x, w = RNG.randint(-128, 127), RNG.randint(-128, 127)
        acc = RNG.randint(-(1 << 19), (1 << 19) - 1)
        valid, rst = RNG.randrange(2), int(cycle == 120)
        await edge(dut, x=x & 255, weight=w & 255,
                   acc_in=acc & ((1 << 20) - 1), in_valid=valid, rst=rst)
        assert int(dut.out_valid.value) == bool(valid and not rst)
        if valid and not rst:
            assert int(dut.result.value) == (acc + x * w) & ((1 << 20) - 1)

async def check_weights(dut):
    active = shadow = 0
    for cycle in range(180):
        load, swap, value = RNG.randrange(2), RNG.randrange(2), RNG.randrange(256)
        await FallingEdge(dut.clk)
        dut.load.value, dut.swap.value, dut.weight_in.value = load, swap, value
        await ReadOnly()
        assert int(dut.selected.value) == (shadow if swap else active)
        active, shadow = (shadow if swap else active), (value if load else shadow)
        await RisingEdge(dut.clk)
        await ReadOnly()
        assert int(dut.active.value) == active
        assert int(dut.shadow.value) == shadow

async def check_sum(dut):
    for count in (0, 1, 2, 3, 17, 31):
        await edge(dut, start=1, command_count=count, in_valid=0)
        total, taken = 0, 0
        while taken < count:
            valid, value = RNG.randrange(2), RNG.randrange(256)
            await edge(dut, start=1, command_count=7, in_valid=valid, in_data=value)
            if valid:
                taken += 1
                total += value
            assert int(dut.done.value) == (taken == count)
            assert int(dut.sum.value) == total
        assert int(dut.done.value) == 1
        assert int(dut.sum.value) == total
        await edge(dut, start=0, in_valid=0)
        assert int(dut.busy.value) == 0
    await edge(dut, start=1, command_count=31)
    await edge(dut, start=0, in_valid=1, in_data=19)
    await reset(dut)
    assert int(dut.busy.value) == 0 and int(dut.sum.value) == 0

@cocotb.test()
async def independent_cycle_model(dut):
    top = os.environ["CASE"]
    if top == "lane_adders":
        for _ in range(200):
            a = [RNG.randrange(256) for _ in range(2)]
            b = [RNG.randrange(256) for _ in range(2)]
            dut.a.value = a[0] | (a[1] << 8)
            dut.b.value = b[0] | (b[1] << 8)
            await Timer(1, unit="ns")
            assert int(dut.y.value) == (a[0] + b[0]) | ((a[1] + b[1]) << 9)
        return
    initial = {
        "counter": {"en": 0},
        "rv_register": {"in_valid": 0, "in_data": 0, "out_ready": 0},
        "sync_fifo": {"in_valid": 0, "in_data": 0, "out_ready": 0},
        "sync_ram": {"wr_en": 0, "rd_en": 0, "wr_addr": 0, "rd_addr": 0, "wr_data": 0},
        "mac": {"x": 0, "weight": 0, "acc_in": 0, "in_valid": 0},
        "weight_bank": {"load": 0, "swap": 0, "weight_in": 0},
        "stream_sum": {"start": 0, "command_count": 0, "in_valid": 0, "in_data": 0},
    }[top]
    dut.rst.value = 1
    for key, value in initial.items():
        getattr(dut, key).value = value
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())
    await ClockCycles(dut.clk, 2)
    await FallingEdge(dut.clk)
    dut.rst.value = 0
    check = {"counter": check_counter, "rv_register": check_stream,
             "sync_fifo": check_stream, "sync_ram": check_ram,
             "mac": check_mac, "weight_bank": check_weights,
             "stream_sum": check_sum}[top]
    await check(dut)
