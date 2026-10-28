# 🕸️📊 Day 2: Data Acquisition & Exploratory Visualization

Welcome to Day 2 of the Data Analytics and Visualization Workshop! Today is all about two fundamental skills for any data scientist: **getting data from the web** and creating the first, crucial **visualizations to understand it**.

This repository contains all the notebooks and resources for today's sessions.

## 📋 Table of Contents

*   [**🌞 Pre-Lunch Session: Web Dataraping Dynamic Sites with `Selenium`:**
    *   Understanding why `requests` fails on sites that use JavaScript to load content.
    *   Automating a real browser (in "headless" mode) to let the JavaScript run.
    *   Techniques for interacting with a page: clicking buttons, filling out login forms, and handling **infinite scroll** to load more data.

---

## 📈 Part 2: Exploratory Visualization - Telling Stories with Plots

Once we have data, our next step is to explore it visually. This session covers the foundational tools for plotting in Python, moving from basic building blocks to powerful statistical graphics.

### Key Concepts Covered:

*   **`Matplotlib` Fundamentals:**
    *   **Anatomy of a Plot:** Understanding the relationship between the `Figure` (the whole window) and the `Axes` (the actual plot).
    *   **Basic Plot Types:** Creating essential plots like `line`, `bar`, and `scatter` plots from scratch.
    *   **Customization:** Learning to add `labels`, `titles`, `legends`, and text `annotations` to make your plots clear and professional.

*   **`Seaborn` for Statistical Graphics:**
    *   Building on top of Matplotlib, Seaborn provides a high-level interface for creating beautiful and informative statistical plots.
    *   **One-Liners for Complex Plots:** Quickly generating `boxplots`, `violin plots` (for distribution), `heatmaps` (for correlations), and `pairplots` (for seeing relationships across all variables).
    *   **Aesthetics:** Using built-in color palettes and themes to drastically improve plot readability.

*   **Best Practices in Visualization:**
    *   **Choosing the Right Plot:** Matching your question to the most effective plot type.
    *   **Facets & Subplots:** Arranging multiple plots in a grid for easy comparison.
    *   **Avoiding "Chart Junk":** Focusing on data-ink and creating clean, uncluttered visualizations.

---

## 💻 Hands-On Labs

This directory contains two hands-on labs to solidify your learning.

###  Lab 2A: Scraping an E-commerce Site
*   **Objective:** Scrape product information (e.g., product name, price, rating, and number of reviews) from a sample e-commerce website.
*   **Tools:** `requests`, `BeautifulSoup`, `pandas`
*   **File:** `lab-2a-scraping.ipynb`

### Lab 2B: Visualizing Sales Data
*   **Objective:** Use the cleaned dataset from Day 1 to explore sales patterns. Create bar charts for sales by region, histograms for price distribution, and a correlation heatmap.
*   **Tools:** `matplotlib`, `seaborn`, `pandas`
*   **File:** `lab-2b-visualization.ipynb`

---

## 🛠️ Setup & Requirements

Before running the notebooks, please ensure you have the necessary libraries installed. You can install them using pip.

1.  **Create a `requirements.txt` file with the following content:**
    ```
    pandas
    requests
    beautifulsoup4
    selenium
    matplotlib
    seaborn
    notebook
    ```

2.  **Install the libraries from the terminal:**
    ```bash
    pip install -r requirements.txt
    ```

> **Special Note on Selenium:**
> Selenium requires a **WebDriver** to control a browser. You need to download the WebDriver for the browser you want to use (e.g., ChromeDriver for Google Chrome). For a simpler setup, we recommend using a library like `webdriver-manager` which can handle this automatically.
>
> To install it: `pip install webdriver-manager`

## 🚀 How to Run the Code

1.  **Clone the repository** to your local machine.
2.  Navigate to the `Day_02` directory in your terminal.
3.  **Install the required libraries** as described in the Setup section.
4.  **Launch Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
5.  Open the lab notebooks (`.ipynb` files) and start experimenting
    ```

3.  **Install Required Libraries**
    *We have provided a `requirements.txt` file to make this easy.*
    ```bash
    pip install -r requirements.txt
    ```

4.  **Setup Selenium WebDriver**
    *Selenium requires a "WebDriver" to control a browser. The most common is ChromeDriver.*
    - Ensure you have Google Chrome installed.
    - Download the ChromeDriver that **matches your Chrome browser version** from the [official Chrome for Testing dashboard](https://googlechromelabs.github.io/chrome-for-testing/).
    - Unzip the downloaded file and place `chromedriver.exe` (or `chromedriver` on Mac/Linux) in a known location on your system, or directly in this project folder.

5.  **Launch Jupyter Notebook**
    ```bash
    jupyter notebook
    ```
    This will open a new tab in your browser. Navigate into the `notebooks/` directory and start with the first notebook
