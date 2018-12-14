library(lattice)

read.table("output-throughput-latency/stats.csv", header=TRUE) -> csvDataFrameSource
csvDataFrame <- csvDataFrameSource

trellis.device("pdf", file="graph1.pdf", color=T, width=6.5, height=5.0)

xyplot(csvDataFrame$requests~csvDataFrame$rate,
       xlab="Request Rate",
       ylab="Throughput",
       col="red",
       pch = 19,
       type='b')
# ... xyplot here

dev.off() -> null 

trellis.device("pdf", file="graph2.pdf", color=T, width=6.5, height=5.0)

xyplot(csvDataFrame$latency~csvDataFrame$requests,
       xlab="Throughput",
       ylab="Latency",
       col="red",
       pch = 19,
       type='b')
# ... xyplot here

dev.off() -> null 
