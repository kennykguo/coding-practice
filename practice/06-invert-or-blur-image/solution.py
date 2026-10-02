# Problem statement: README.md   |   Run tests: python3 test.py


def transform_image(image: list[list[int]], operation: str) -> list[list[int]]:
    
    rows = len(image)
    cols = len(image[0])
    if operation == "invert":
        for i in range(len(image)):
            # over all rows

            l = 0
            r = len(image[0]) - 1

            while l < r:
                # swap left and right
                temp = image[i][l]
                image[i][l] = image[i][r]
                image[i][r] = temp
        return image

    else:
        
        copy_image = [[ 0 for i in range(len(image[0]))] for j in range(len(image))]
        print(copy_image) # WHY did copy_image = image.copy() not work?

        for i in range(rows):
            for j in range(cols):
                
                total = 0
                count = 0

                # at a single pixel, look all directions - 8 total
                for dr, dc in [(0, 1), (1,0), (-1,0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                    r = i + dr
                    c = j + dc

                    if r >= 0 and r< rows and c >= 0 and c < cols:
                        total +=image[r][c]
                        count +=1
                    
                print(i, j)
                print(total)
                print(count)
                copy_image[i][j] = total // count if count !=0 else image[i][j]
    
    return copy_image


