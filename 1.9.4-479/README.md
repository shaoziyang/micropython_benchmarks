# micropython 1.9.4-479

## micropython version

microbit
* 1.9.2

ESP32 Lobo
* 3.20.20

All other device
* 1.9.4-479

## Test item

* Integer addition 1000,000 times
* Float addition 1000,000 times
* Integer multiplication 1000,000 times
* Float multiplication 1000,000 times
* Integer division 1000,000 times
* Float division 1000,000 times
* 1000 digit Pi calculation
* 5000 digit Pi calculation
* 100,000 digit Pi calculation

## Result

|                 |MCU      |Freq|Int Add|Float Add|Int Mul|Float Mul|Int div|Float Div|Pi:1000|Pi:5000|Pi:100000|
|:---             |:---     |:---|:----: |:----:   |:----: |:----:   |:----: |:----:   |:----: |:----: |:----:   |
|**microbit**     |nRF51822 |16M |61.89  |78.03    |71.59  |81.60    |67.95  |106.87   |10.98  |-      |-        |
|**Nucleo_F411**  |STM32F411|96M |5.86   |13.96    |6.07   |14.02    |6.07   |14.07    |1.25   |19.03  |-        |
|**PYBV10**       |STM32F405|168M|3.44   |7.93     |3.56   |7.97     |3.56   |8.13     |0.67   |10.8   |-        |
|**Nucleo_L432KC**|STM32LM32|32M |20.86  |46.35    |21.49  |46.55    |21.95  |46.71    |2.60   |49.44  |-        |
|**STM32L476DISC**|STM32L476|80M |8.59   |18.34    |8.99   |18.42    |8.93   |18.49    |1.37   |21.45  |-        |
|**STM32F7DISC**  |STM32F746|192M|1.93   |5.16     |2.45   |5.08     |2.12   |5.39     |0.21   |5.42   |4276.47  |
|**Nucleo_H743**  |STM32H743|400M|0.86   |1.96     |0.94   |1.98     |0.91   |2.07     |0.11   |4.66   |1004.32  |
|**ESP8266**      |ESP8266  |80M |15.55  |18.34    |17.96  |18.92    |16.96  |21.46    |2.09   |40.22  |-        |
|**ESP32**        |ESP32    |240M|2.61   |4.42     |2.79   |4.42     |2.72   |4.66     |0.57   |8.41   |-        |
|**ESP32 psRAM**  |ESP32    |240M|3.37   |7.96     |3.55   |17.88    |15.25  |8.32     |0.67   |18.01  |12394.50 |
|**K210**         |K210C    |    |8.19   |8.76     |8.23   |8.74     |7.75   |8.76     |0.12   |2.82   |1480.96  |

* More result please see [benchmark.xlsx](benchmarks.xlsx).  
