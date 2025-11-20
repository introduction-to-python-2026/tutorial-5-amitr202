# Q: Write an import statement that imports the function pyplot from the module matplotlib and renames it to plt.

def build_histogram(data):
    def build_histogram(data):
    my_dict = {}
    for num in data:
      if num in my_dict:
        my_dict[num] += 1
      else:
        my_dict[num] = 1
    return my_dict

def plot_histogram(histogram):
    import matpliotlib.pypot as plt
    x_values = list(histogram.keys())
    y_values = list(histogram.values())

    plt.bar(x_values, y_values)
    plt.xlabel('Items')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()


