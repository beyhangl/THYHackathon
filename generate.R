fileConn<-file("C:\\Users\\asus\\Desktop\\RandomCDR\\first.txt")
path="C:\\Users\\asus\\Desktop\\RandomCDR\\first.txt"


library(shiny)
library(stringr)
a=1
testit <- function(x)
{
  p1 <- proc.time()
  Sys.sleep(x)
  proc.time() - p1 # The cpu usage should be negligible
}

while (TRUE)
{
  #testit(1)
  yas=toString(floor(runif(1, 24, 65)))
  if (yas >60)
  {
    sirket=toString(floor(runif(1, 0, 0)))
  }
  else
  {
    sirket=toString(floor(runif(1, 0, 25)))
  }
  if (yas >45)
  {
    evcil_hayvan=toString(floor(runif(1, 0, 1)))
    esya=toString(floor(runif(1, 0, 0)))
    universite=toString(floor(runif(1, 0, 0)))
    twitter1=toString(floor(runif(1, 0, 0)))
    twitter2=toString(floor(runif(1, 0, 0)))
    twitter3=toString(floor(runif(1, 0, 0)))
    
  }
  else
  {
    evcil_hayvan=toString(floor(runif(1, 0, 2)))
    esya=toString(floor(runif(1, 0, 15)))
    universite=toString(floor(runif(1, 0, 200)))
    twitter1=toString(floor(runif(1, 0, 100)))
    twitter2=toString(floor(runif(1, 0, 100)))
    twitter3=toString(floor(runif(1, 0, 100)))
    
  }
  if (yas >28)
  {
    evlilik=toString(floor(runif(1, 0, 2)))
    durum=toString(floor(runif(1, 2, 4)))
    if (yas >58)
    {
      durum=toString(floor(runif(1, 3, 4)))
    }
  }
  else
  {
    evlilik=toString(floor(runif(1, 0, 1)))
    durum=toString(floor(runif(1, 1, 2)))
  }
  if (yas <35 & yas>28)
  {
     cocuk_yas=toString(floor(runif(1, 0, 6)))
  }
  else
  {
    cocuk_yas=toString(floor(runif(1, 0, 1)))
  }  
  text=paste(toString(floor(runif(1, 10389583204,66349001436 ))),yas,toString(floor(runif(1, 1, 81))),toString(floor(runif(1, 0, 2))),evlilik,toString(floor(runif(1, 1, 81))),durum,toString(floor(runif(1, 1, 6))),toString(floor(runif(1, 1, 8))),cocuk_yas,universite,sirket,esya,evcil_hayvan,twitter1,twitter2,twitter3,toString(floor(runif(1, 0, 10))),toString(floor(runif(1, 0, 10))),sep = ",")
  write(text, file=path,append = TRUE)
  control<-runif(1, 1, 200)
  if(control>=199)
  {
    a=a+1
    close(fileConn)
    path=paste("C:\\Users\\asus\\Desktop\\RandomCDRR\\",toString(a),".txt")
    path<-gsub(" ", "", path, fixed = TRUE)
    fileConn<-file(path)
    write(text, file=fileConn,append=TRUE)
  }
}


