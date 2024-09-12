import parser_data
from plot_data import plot_data



def clean_data(data):
    print ("Write code to remove garbage data")
    # data is a 500Hz list of tuples (time, X, Y, Z)
    # we want to throw out the first and last five seconds of data
    trim_start_time = trim_stop_time = 5
    freq = 500
    data = data[trim_start_time*freq:-trim_stop_time*freq]


    print ("Create new file without garbage data and save it in data folder")
    file_name_clean = "ours/walking_steps_clean.csv"

    with open("data/" + file_name_clean, "w") as f:
        f.write("time,X,Y,Z\n")
        for row in data:
            f.write("{},{},{},{}\n".format(row[0], row[1], row[2], row[3]))




def main():
    # Get data
    file_name = "walking_steps.csv"  # Change to your file name
    data = parser_data.get_data(file_name) #data -- time,X,Y,Z
    clean_data(data)


if __name__== "__main__":
  main()

