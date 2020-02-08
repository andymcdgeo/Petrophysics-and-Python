#calculate porosity using density

class Petrophysics():
    def __init__(self):
        print("Welcome to the Petrophysical Calculator")

    def getMatrix(self):
        while True:
            try:
                matrixOfRes = input("What is the dominant lithology of your reservoir? Enter Sst, Lmst or Dol:   ")
            except TypeError:  # Line doesn't seem to work
                print("Letters only please!")
                continue
            if matrixOfRes.lower() == "sst" or matrixOfRes.lower() == "lmst" or matrixOfRes.lower() == "dol":
                break
            else:
                print("Try again")
                continue

        return matrixOfRes

    def Porosity(self, matrix, Rhob, Rhofl):
        matrixVals = {"sst": 2.65, "lmst": 2.71, "dol": 2.85}

        Rhoma = matrixVals.get(matrix.lower())

        porosity = (Rhoma - Rhob) / (Rhoma - Rhofl)
        #print(porosity)

        return porosity, Rhoma

    def WaterSatArchie(self, porosity, a, m, n, Rt, Rw):

        partA = a / (porosity ** m)
        partB = Rw / Rt

        waterSat = (partA * partB) ** (1/n)

        #print(waterSat)
        return waterSat

# Initialise the Petrophysics class
petrophysics = Petrophysics()
bulkDensity = 2.45
Rt = 100
Rw = 0.1
archieA = 1
archieM = 2
archieN = 2

#Obtain RhoMatrix, Phit and Sw
matrix = petrophysics.getMatrix()
Phit, Rhoma = petrophysics.Porosity(matrix, bulkDensity, 1.0)
Sw = petrophysics.WaterSatArchie(Phit, archieA, archieM, archieN, Rt, Rw)

print("For a Bulk Density of {}g/cc and a Matrix of {}g/cc: \n "
      "Porosity = {}% \n" .format(bulkDensity, Rhoma, round(Phit * 100, 2)))

print("Archie Water Saturation with a, m and n as {}, {}, {}, an Rt of {}ohm.m and an Rw of {}ohm.m \n"
      " Sw = {}%"
      .format(archieA, archieM, archieN, Rt, Rw, round(Sw * 100, 2)))

