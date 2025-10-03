# BIG-DATA-ANALYSIS

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: MOHAMED SAFEER ANFAL . C

*INTERN ID*: CT04DY2161

*DOMAIN*: Data Analytics

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

*DESCRIPTION*:Project Description: Big Data Analysis on Covid-19 using Dask and Pandas

The project demonstrates the use of Python libraries to analyze large-scale Covid-19 data efficiently. The primary focus is on big data processing using the Dask library, supported by Pandas for data handling and exporting results, while the OS library manages file storage. Together, these libraries create a workflow that can handle massive datasets, clean and preprocess the data, and extract meaningful insights.

1. Dask (dask.dataframe)

The heart of this project is the Dask library. Dask is a flexible parallel computing library in Python that enables processing of datasets much larger than the available memory by breaking them into smaller partitions and executing computations in parallel. Unlike Pandas, which loads the entire dataset into memory, Dask allows us to work on datasets too large for RAM by using lazy evaluation and parallelism.

In this project, Dask is used to:

Load the Covid-19 dataset using dd.read_csv(). Instead of reading all data at once, the file is split into partitions, allowing parallel computation.

Perform scalable data cleaning, such as converting columns to numeric using dd.to_numeric() and filling missing values with .fillna().

Execute analytical tasks like finding the top 5 countries with the highest confirmed cases, deaths, and recoveries using .nlargest().

Perform group-level operations such as calculating the average death and recovery ratios per WHO region and computing the maximum active case ratio per region.

These operations show Dask’s power in handling big data analysis that would otherwise be computationally expensive with Pandas alone.

2. Pandas

Pandas is the most widely used library for data analysis in Python, but its limitation lies in memory usage. Since Dask is built on top of Pandas, once computations are finished in parallel, Dask converts results into Pandas DataFrames using .compute().

In this project, Pandas is crucial for:

Displaying data samples (head()).

Converting the lazy Dask computations into actual tabular results that can be printed and saved.

Exporting outputs to CSV files using .to_csv(), making the results accessible for further analysis or reporting.

Thus, Pandas complements Dask by handling the final, in-memory computations and storage.

3. OS (Operating System Library)

The os module provides a simple way to interact with the operating system. In this project, it is mainly used for:

Creating a results directory (os.makedirs()), ensuring that analysis outputs are organized and stored properly.

Managing file paths when saving multiple CSV results, such as top confirmed cases or regional averages.

This ensures the project is not only computationally effective but also well-structured in terms of output management.

Conclusion

This project highlights the synergy between Dask, Pandas, and OS. Dask handles the heavy lifting by enabling distributed computations on large datasets. Pandas ensures user-friendly data handling and final reporting, while OS manages the storage environment. Together, these libraries provide a complete solution for big data analysis in Python.

The project successfully performs tasks like identifying the worst-hit countries, analyzing recoveries, and calculating averages per region—all while ensuring scalability. This demonstrates how modern libraries empower analysts to transform raw data into actionable insights efficiently.





*OUTPUT*:


<img width="1366" height="729" alt="Image" src="https://github.com/user-attachments/assets/1c534d85-9ae2-43f4-a1b9-978daf13704a" />

<img width="1366" height="685" alt="Image" src="https://github.com/user-attachments/assets/b0c3e8e7-a215-4a1c-a62d-e02981f80f9d" />

<img width="1366" height="685" alt="Image" src="https://github.com/user-attachments/assets/f8712c2d-5328-4eb5-b324-5795da124ca9" />



