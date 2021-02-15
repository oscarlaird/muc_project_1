from plot_data import plot_data
import parser_data

def count_steps(data):
    print("Accelerometer data graph")
    plot_data(data)
    num_steps = 0
    '''
    ADD YOUR CODE HERE. This function counts the number of steps in data and returns the number of steps
    '''
    return num_steps


def main():
    # Get data
    file_name = "test.csv"  # Change to your file name
    data = parser_data.get_data(file_name)
    number_of_steps = count_steps(data)
    print ("Number of steps counted are :{0:d}".format(number_of_steps))

if __name__== "__main__":
  main()

