import plotly.figure_factory as figure_factory
import plotly.graph_objects as graph_objects
import statistics
import pandas
import csv
import random

df = pandas.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)

def mean_sampling(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []

for i in range(0,100):
    set_of_mean = mean_sampling(30)
    mean_list.append(set_of_mean)

stdev = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

print("Sampling Distribution Mean: ", mean)

first_stdev_start, first_stdev_end = mean - stdev, mean + stdev
second_stdev_start, second_stdev_end = mean - 2*stdev, mean + 2*stdev
third_stdev_start, third_stdev_end = mean - 3*stdev, mean + 3*stdev

print("Standard Deviation 1: ", first_stdev_start, "and", first_stdev_end)
print("Standard Deviation 2: ", second_stdev_start, "and", second_stdev_end)
print("Standard Deviation 3: ", third_stdev_start, "and", third_stdev_end)

def plot_graph(mean_list):
    df = mean_list
    fig = figure_factory.create_distplot([df], ['reading_time'], show_hist = False)
    fig.add_trace(graph_objects.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
    fig.add_trace(graph_objects.Scatter(x=[first_stdev_start, first_stdev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
    fig.add_trace(graph_objects.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
    fig.add_trace(graph_objects.Scatter(x=[second_stdev_start, second_stdev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
    fig.add_trace(graph_objects.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
    fig.add_trace(graph_objects.Scatter(x=[third_stdev_start,third_stdev_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
    fig.add_trace(graph_objects.Scatter(x=[third_stdev_end,third_stdev_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
    fig.show()

#plot_graph(mean_list)

df = pandas.read_csv('sample_2.csv')
data = df["reading_time"].tolist()
mean_of_sample2 = statistics.mean(data)
print("Mean of Sample 2: ", mean_of_sample2)
fig = figure_factory.create_distplot([mean_list], ['reading_time'], show_hist = False)
fig.add_trace(graph_objects.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(graph_objects.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="SAMPLE 2 MEAN"))
fig.add_trace(graph_objects.Scatter(x=[first_stdev_start, first_stdev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 START"))
fig.add_trace(graph_objects.Scatter(x=[first_stdev_end, first_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(graph_objects.Scatter(x=[second_stdev_start, second_stdev_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 START"))
fig.add_trace(graph_objects.Scatter(x=[second_stdev_end, second_stdev_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(graph_objects.Scatter(x=[third_stdev_start,third_stdev_start], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 START"))
fig.add_trace(graph_objects.Scatter(x=[third_stdev_end,third_stdev_end], y=[0,0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

z_score = (mean_of_sample2 - mean) / stdev
print("Z-Score: ", z_score)

if(mean_of_sample2 > mean):
    print("Intervention is successful")
elif(mean_of_sample2 < mean):
    print("Intervention is unsuccessful")

