import requests 
import test
from test import Dustbin,Population,GA,TourManager
def getPath():
# r =requests.get('https://cloud.boltiot.com/remote/
eee61832-c0de-414c-8ac9-4db633ae2979/digitalWrite?
pin=0&state=HIGH&deviceName=BOLT13819450') 
# dic = r.json()
# full = dic['full']
# lat = dic['lat']
# lon = dic['long']
# tourmanager = TourManager()
# for i in len(full):
# if (full):
# tourmanager.add(Dustbin(lat[i],lon[i]))
# pop = Population(tourmanager, 50, True);
# # print("Initial distance: " + 
str(pop.getFittest().getDistance()))
# # Evolve population for 50 generations
# ga = GA(tourmanager)
# pop = ga.evolvePopulation(pop)
# for i in range(0, 100):
# pop = ga.evolvePopulation(pop)
# paths = str(pop.getFittest()).split('|')[1:-1]
# fittest = []
# paths = [i.split(',') for i in paths]
# for i in paths:
# fittest.append([float(i[0]),float(i[1].strip())])
# return fittest
tourmanager = TourManager()
# Create and add our cities
dustbin1 = Dustbin(22.320, 87.260)
tourmanager.addDustbin(dustbin1)
dustbin2 = Dustbin(22.334, 87.260)
tourmanager.addDustbin(dustbin2)
dustbin3 = Dustbin(22.338, 87.282)
tourmanager.addDustbin(dustbin3)
dustbin4 = Dustbin(22.316, 87.268)
tourmanager.addDustbin(dustbin4)
dustbin5 = Dustbin(22.316, 87.258)
tourmanager.addDustbin(dustbin5)
dustbin6 = Dustbin(22.318, 87.254)
tourmanager.addDustbin(dustbin6)
dustbin7 = Dustbin(22.312, 87.262)
tourmanager.addDustbin(dustbin7)
dustbin8 = Dustbin(22.302, 87.270)
tourmanager.addDustbin(dustbin8)
dustbin9 = Dustbin(22.340, 87.266)
tourmanager.addDustbin(dustbin9)
dustbin10 = Dustbin(22.330, 87.282)
tourmanager.addDustbin(dustbin10)
dustbin11 = Dustbin(22.338, 87.292)
tourmanager.addDustbin(dustbin11)
dustbin12 = Dustbin(22.296, 87.285)
tourmanager.addDustbin(dustbin12)
dustbin13 = Dustbin(22.288, 87.291)
tourmanager.addDustbin(dustbin13)
dustbin14 = Dustbin(22.300, 87.290)
tourmanager.addDustbin(dustbin14)
dustbin15 = Dustbin(22.306, 87.300)
tourmanager.addDustbin(dustbin15)
dustbin16 = Dustbin(22.302, 87.290)
tourmanager.addDustbin(dustbin16)
dustbin17 = Dustbin(22.302, 87.294)
tourmanager.addDustbin(dustbin17)
dustbin18 = Dustbin(22.301, 87.299)
tourmanager.addDustbin(dustbin18)
dustbin19 = Dustbin(22.328, 87.278)
tourmanager.addDustbin(dustbin19)
dustbin20 = Dustbin(22.325, 87.274)
tourmanager.addDustbin(dustbin20)
# Initialize population
pop = Population(tourmanager, 50, True);
# Evolve population for 50 generations
ga = GA(tourmanager)
pop = ga.evolvePopulation(pop)
for i in range(0, 100):
pop = ga.evolvePopulation(pop)
paths = str(pop.getFittest()).split('|')[1:-1]
fittest = []
paths = [i.split(',') for i in paths]
for i in paths:
fittest.append([float(i[0]),float(i[1].strip())])
return fittest
if __name__ == '__main__':
print(getPath())
