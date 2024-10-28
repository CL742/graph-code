import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import files
uploaded = files.upload()

# Read the Excel file
file_path = "Analysis_sample_fixed.xlsx"
sheet_name = 'in'          # Replace with sheet name

# Load the data into a pandas DataFrame
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Display the first few rows of the DataFrame
print(data.head())

col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, \
col11, col12, col13, col14, col15, col16, col17, col18, col19, \
col20, col21, col22, col23, col24, col25, col26, col27, col28 = data.columns

#OverNumber = data[col1]
#BallNumber = data[col2]
#BowlerName = data [col3]
#BatsmanName = data [col4]
#BatsmanHand = data [col5]
BowlerReleaseSpeed = data [col6]
BounceX = data [col7]
BounceY = data [col8]
StumpsY = data [col9]
StumpsZ = data [col10]
Swing = data [col11]
Deviation = data [col12]
#RunsScored = data [col13]
#ShotLandingX = data [col14]
#ShotLandingY = data [col15]
#TrajectoryTime = data [col16]
#TrajectoryDate = data [col17]
BounceVelocity = data [col18]
OutOfBounceAngle = data [col19]
DropAngle = data [col20]
AngleLeavingBowlersHand = data [col21]
#ShotPlayed = data [col22]
#ShotType = data [col23]
BowlerReleaseYPosition = data [col24]
BowlerReleaseZPosition = data [col25]
AccelerationY = data [col26]
AccelerationZ = data [col27]
var28 = data [col28]


print(BowlerReleaseSpeed)

plt.figure(figsize=(10, 6))
plt.title = "Ball Bounce Position"
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")

plt.scatter(BounceX, BounceY, label='Bounce Position')  # Adjusted plot command
plt.legend()
plt.grid()
plt.show()
