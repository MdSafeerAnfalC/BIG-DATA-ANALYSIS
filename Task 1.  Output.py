Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=================== RESTART: E:\CodTech\Final Task\Task 1.py ===================
Dask Analysis on Covid - 19...

--- Data Loaded with Dask ---
       Country  Confirmed  ...  1 week % increase             WHO Region
0  Afghanistan      36263  ...               2.07  Eastern Mediterranean
1      Albania       4880  ...              17.00                 Europe
2      Algeria      27973  ...              18.07                 Africa
3      Andorra        907  ...               2.60                 Europe
4       Angola        950  ...              26.84                 Africa

[5 rows x 15 columns]
Number of partitions: 1
Dask DataFrame dtypes:
Country                   string[pyarrow]
Confirmed                           int64
Deaths                              int64
Recovered                           int64
Active                              int64
New cases                           int64
New deaths                          int64
New recovered                       int64
Deaths / 100 Cases                float64
Recovered / 100 Cases             float64
Deaths / 100 Recovered            float64
Confirmed last week                 int64
1 week change                       int64
1 week % increase                 float64
WHO Region                string[pyarrow]
dtype: object

--- Data Preprocessing  ---

--- Task 1: Top 5 Countries by Confirmed Cases ---
          Country  Confirmed
173            US    4290259
23         Brazil    2442375
79          India    1480073
138        Russia     816680
154  South Africa     452529

--- Task 2: Top 5 Countries by Deaths ---
            Country  Deaths
173              US  148011
23           Brazil   87618
177  United Kingdom   45844
111          Mexico   44022
85            Italy   35112

--- Task 3: Top 5 Countries by Recovered Cases ---
    Country  Recovered
23   Brazil    1846641
173      US    1325804
79    India     951166
138  Russia     602249
35    Chile     319954

--- Task 4: Average Metrics per WHO Region ---
                       Deaths / 100 Cases  Recovered / 100 Cases
WHO Region                                                      
Africa                           2.306458              57.014792
Americas                         3.052571              62.291429
Eastern Mediterranean            3.563182              66.593182
Europe                           4.198393              68.635000
South-East Asia                  1.296000              66.704000
Western Pacific                  1.290000              76.805000

--- Demonstrating the complex Dask operation  ---

Max Active Ratio per WHO Region:
WHO Region
Africa                   0.993533
Americas                 0.923200
Eastern Mediterranean    0.940653
Europe                   0.977507
South-East Asia          1.000000
Western Pacific          0.822581
Name: Active_Ratio, dtype: float64

 Big Data Analysis Has Completed Using Dask. 
>>> 