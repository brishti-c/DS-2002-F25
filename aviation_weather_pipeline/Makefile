.PHONY: all fetch analyze clean

# Default target
all: analyze

fetch:
	@echo "=== Fetching METAR data... ==="
	./fetch_metars.sh
	@echo "=== Fetch complete. Raw data saved in raw_metars/ ==="

analyze: fetch
	@echo "=== Analyzing METAR data... ==="
	./analyze_data.sh
	@echo "=== Analysis complete. Results saved in weather_report.csv ==="
	@echo "=== Pipeline completed successfully! ==="

clean:
	@echo "=== Cleaning up generated data... ==="
	rm -rf raw_metars weather_report.csv
	@echo "=== Cleanup complete. ==="

