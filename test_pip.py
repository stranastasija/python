from progress.bar import FillingCirclesBar
import time

bar = FillingCirclesBar('Processing', max=20)
for i in range(20):
    time.sleep(1)
    bar.next()
bar.finish()