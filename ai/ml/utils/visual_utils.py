import matplotlib.pyplot as plt


def show_grid_via_matplotlib(rows: 'no of rows', columns: 'no of columns of the grid', image_name_image_dict: 'dictionary with key as image name and value as numpy object of image', get_cmap_value: 'cmap color type for pyplot.get_cmap parameter') -> 'pyplot object':
    f, axarr = plt.subplots(rows, columns)
    image_names, images = list(image_name_image_dict), list(image_name_image_dict.values())
    for row in range(rows):
        for column in range(columns):
            image_index = ((row) * (columns)) + (column)
            axarr[row, column].imshow(images[image_index])
            axarr[row, column].set_title(image_names[image_index])
    return plt
