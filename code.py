# Import necessary libraries for data manipulation, visualization, and numerical computations
import pandas as pd  # Data manipulation and analysis
import matplotlib.pyplot as plt  # Plot creation and visualization
import numpy as np  # Numerical computations

# Load energy consumption data from an Excel file
#energyConsumption = pd.read_excel('/content/energyconsumption.xlsx')

energyConsumption = pd.read_excel('energyconsumption.xlsx')

# Display information about the energy consumption DataFrame
print(energyConsumption.info())

# Display descriptive statistics for the energy consumption DataFrame
print(energyConsumption.describe())

def cleaning(data):
    """
    Cleans the DataFrame by removing unwanted rows and columns
    that complicate data access and rounds numerical values.

    Parameters:
        data (DataFrame): The input DataFrame to be cleaned.

    Returns:
        DataFrame: The cleaned DataFrame with selected rows and columns.
    """
    data = data.iloc[1:-4, 0:-3]
    data = data.round()
    return data


def newIndex(data):
    """
    Sets a new index for the DataFrame using the first column,
    renames the index to 'Name', and removes the original column.

    Parameters:
        data (DataFrame): The input DataFrame for which to set a new index.

    Returns:
        DataFrame: The modified DataFrame with a new index.
    """
    index = data.iloc[:, 0]
    indexCopy = index.copy()
    indexCopy.iloc[0] = "Name"
    data = data.set_index(indexCopy)
    data.index.name = "Name"
    data = data.drop("Unnamed: 0", axis=1)
    return data


def newColumn(data):
    """
    Replaces column names in the DataFrame using values from a specified row,
    converts the new column names to integers, and removes the used row.

    Parameters:
        data (DataFrame): The input DataFrame for which to set new column names.

    Returns:
        DataFrame: The modified DataFrame with updated column names.
    """
    col = data.loc["Name"]
    colcopy = col.copy()
    colcopy = colcopy.astype(int)
    data = data.rename(columns=colcopy)
    data = data.drop("Name", axis=0)
    return data


# Define the dataExtraction function to extract data for a specified column
def dataExtraction(data, columnName):
    """
    Extracts data for a specified column from the DataFrame and returns
    it as a list.

    Parameters:
        data (DataFrame): The input DataFrame.
        columnName (str): The name of the column to extract data from.

    Returns:
        list: A list containing the extracted data for the specified column.
    """
    emptyList = []  # Initialize an empty list

    for i in years:
        # Retrieve and append data for each year
        l = data[columnName].loc[i]
        emptyList = np.append(emptyList, l)
    return emptyList

# Apply the cleaning function to remove unwanted rows and columns from the DataFrame
energyConsumption = cleaning(energyConsumption)

# Set a new index for the DataFrame using the first column and remove the original column
energyConsumption = newIndex(energyConsumption)

# Update column names based on a specified row and remove the row afterward
energyConsumption = newColumn(energyConsumption)

# Display the first few rows of the modified DataFrame
print(energyConsumption.head())

# Display the correlation matrix of the energy consumption DataFrame
print(energyConsumption.corr())

# Create a new figure with specified size and resolution
plt.figure(figsize=(12, 6), dpi=310)

# Plot energy consumption data for different regions with distinct styles
# World: blue color, solid line
plt.plot(
    energyConsumption.columns,
    energyConsumption.loc["World"],
    "b",
    label="World"
)

# G7: black color, dashed line
plt.plot(
    energyConsumption.columns,
    energyConsumption.loc["G7"],
    "k--",
    label="G7"
)

# BRICS: red color, dotted line
plt.plot(
    energyConsumption.columns,
    energyConsumption.loc["BRICS"],
    "r:",
    label="BRICS"
)

# European Union: yellow color, dash-dot line
plt.plot(
    energyConsumption.columns,
    energyConsumption.loc["European Union"],
    "y-.",
    label="EU"
)

# Add axis labels and a title to the plot
plt.xlabel("Year (1990-2020)")
plt.ylabel("Energy Consumption (Mtoe)")
plt.title("Total Energy Consumption by Region")

# Enable grid and set x-axis limits
plt.grid(True)
plt.xlim(1989, 2021)

# Add a legend to identify the plotted lines
plt.legend()

# Save the plot as a PNG file and display it
plt.savefig("energyConsumption1.png", dpi=310)
plt.show()

# Transpose the energyConsumption DataFrame for easier access by years
energyConsumption = energyConsumption.T

# Define the list of years for analysis
years = [1990, 1995, 2000, 2005, 2010, 2015, 2020]

# Call the dataExtraction function to retrieve data for different categories
BRICS = dataExtraction(energyConsumption, "BRICS")
G7 = dataExtraction(energyConsumption, "G7")
EU = dataExtraction(energyConsumption, "European Union")
World = dataExtraction(energyConsumption, "World")

# Define colors for each category
colors = ['blue', 'green', 'red', 'orange']

# Set bar width and calculate positions for each category
bar_width = 0.15
index = np.arange(len(years))

# Create a bar chart for energy production by category and year
plt.figure(figsize=(10, 6))

# Plot bars for each category at specific positions
plt.bar(index - 1.5 * bar_width, World, width=bar_width, color=colors[0],
        label='World')
plt.bar(index - 0.5 * bar_width, G7, width=bar_width, color=colors[1],
        label='G7')
plt.bar(index + 0.5 * bar_width, BRICS, width=bar_width, color=colors[2],
        label='BRICS')
plt.bar(index + 1.5 * bar_width, EU, width=bar_width, color=colors[3],
        label='EU')

# Customize plot appearance
plt.xlabel('Year')
plt.ylabel('Energy Consumption (Mtoe)')
plt.title('Total Energy Consumption ')
plt.xticks(index, years)
plt.legend()
plt.tight_layout()

# Save the plot as a PNG file and display it
plt.savefig("energyConsumption2.png", dpi=310)

# Display the plot
plt.show()

# Extract the list of years from the DataFrame index
years = energyConsumption.index.tolist()

# Define colors for each category
colors = ['blue', 'green', 'red', 'orange']

# Create a box plot for energy production by category
plt.figure(figsize=(10, 6))

plt.boxplot(
    [World, G7, BRICS, EU],
    labels=['World', 'G7', 'BRICS', 'EU'],
    patch_artist=True,
    boxprops=dict(facecolor='lightblue'),
    capprops=dict(color='black'),
    whiskerprops=dict(color='black'),
    flierprops=dict(markerfacecolor='red', marker='o'),
    medianprops=dict(color='black')
)

# Customize plot appearance
plt.xlabel('Categories')
plt.ylabel('Energy Consumption (Mtoe)')
plt.title('Box Plot of Energy Consumption')
plt.tight_layout()

# Save the plot as a PNG file and display it
plt.savefig("energyConsumption3.png", dpi=310)

# Display the plot
plt.show()