# App Store Scraper

This repository contains tools for scraping mobile app stores, including **Myket** and **Cafebazaar**. The project is designed to collect app and game data for analysis or other purposes. The scraping process utilizes **Selenium** for web automation and API integration for efficient data retrieval.

## Features

1. **Myket Scraper**:
   - Built using **Selenium** for automated web scraping.
   - Extracts app and game metadata such as name, developer, rating, and download count.
   - Runs seamlessly on **GitHub Actions**, enabling automated and scheduled scraping.

2. **Cafebazaar API Scraper**:
   - Collects app and game information by making direct API calls.
   - Efficient and fast, retrieving structured data with minimal overhead.

## Requirements

### General Requirements
- Python 3.10+
- pip (Python package manager)

### Python Libraries
The project depends on the following libraries:
- **Selenium**: For Myket scraping.
- **Requests**: For making API calls.
- **Pandas**: For data manipulation and storage.
- **GitHub Actions Workflow**: For automating scraping tasks.

### Browser Driver
For Selenium to function correctly, ensure you have the appropriate WebDriver installed for your browser (e.g., ChromeDriver for Google Chrome).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/moein-keyvani-pur/scraping_apps_stores.git
   cd scraping_apps_stores
   ```

2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Download and configure the Selenium WebDriver for your browser.

## Usage

### Myket Scraper
1. Update the target URLs in the Myket scraping script (`myket_scraper.py`).
2. Run the script:
   ```bash
   python myket_scraper.py
   ```
4. The data will be saved as a CSV file in the `output` directory.

### Cafebazaar API Scraper
1. Configure the API endpoint and parameters in the script (`cafebazaar_api_scraper.py`).
2. Run the script:
   ```bash
   python cafebazaar_api_scraper.py
   ```
3. The data will be saved as a JSON or CSV file in the `output` directory.

### Automating with GitHub Actions
1. Set up GitHub Actions by configuring the `selenium.yml` file in the `.github/workflows/` directory.
2. Push the changes to your repository:
   ```bash
   git add .
   git commit -m "myket-run GitHub Actions"
   git push origin main
   ```
3. The workflow will automatically execute the scraper according to the defined schedule.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements or bug fixes. Please ensure that your contributions align with the repository's coding standards and add appropriate documentation.


## Acknowledgments

- **Selenium** for web automation.
- **GitHub Actions** for seamless CI/CD integration.
- **Requests** for API-based data collection.

