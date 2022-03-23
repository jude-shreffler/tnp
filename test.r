print("Creating Charts", quote = FALSE)

scrapedData <- read.table("scrape.csv")

repCount <- scrapedData[1L,1L]
demCount <- scrapedData[2L,1L]
othCount <- scrapedData[3L,1L]
totCount <- repCount + demCount + othCount

repPercent <- as.integer((repCount/totCount*100) + 0.5)
demPercent <- as.integer((demCount/totCount*100) + 0.5)
othPercent <- as.integer((othCount/totCount*100) + 0.5)

if(repPercent + demPercent + othPercent != 100) {
    #fix it
}

pieLabels <- c(paste("Republicans: ", toString(repPercent), "%", sep = ""), paste("Democrats: ", toString(demPercent), "%", sep = ""), paste("Other: ", toString(othPercent), "%", sep = ""))

png("scrapedPie.png", width = 2240L, height = 1920L)

pie(c(repCount, demCount, othCount), labels = pieLabels, col = c("red", "blue", "grey"), main = "Candidate Party Data by Percent", radius = 0.9, cex = 5L, cex.main = 5L)

dev.off()