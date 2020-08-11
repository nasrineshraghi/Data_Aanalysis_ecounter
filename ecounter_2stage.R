library(stream)
library(animation)
library(gganimate)
library(ggplot2)

## Loading Data into Stream (DSD)
stream <- DSD_ReadCSV("C:/Users/neshragh/ecounter/Affinity_Sample_SPY/micro_during - Copy.csv", sep=",", header = TRUE, loop=TRUE)


#### Creating the DSC object
win_km <- DSC_TwoStage(
  micro=DSC_Window(lambda=0.0333),
  macro=DSC_Kmeans(k=4)
)
win_km

update(win_km, stream, 64000)
plot(win_km, stream, type="both")
animate_cluster(win_km, stream,n=64000, xlim=c(0,160), ylim=c(0,160))