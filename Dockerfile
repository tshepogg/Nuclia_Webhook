# Use the official Python image as the base
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Set environment variables for API key and Knowledge Box ID
ENV NUCLIA_API_KEY="eyJhbGciOiJSUzI1NiIsImtpZCI6InNhIiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwczovL2V1cm9wZS0xLm51Y2xpYS5jbG91ZC8iLCJpYXQiOjE3MzA5MTM4NzYsInN1YiI6IjNiZWNiNzA0LWNhZDktNGRkOC1hNWM3LWE4M2UzYTQxYTZlOCIsImp0aSI6ImEyZTFlMTAwLTA2MmYtNDk1MS1hN2M2LTUzNDI2YWNlYjZlOCIsImV4cCI6MTc2MjQ0OTg3Niwia2V5IjoiODI3ODNlYTAtOGM0NC00MzgxLTg0MTYtMGZiOTliOGViYzZhIiwia2lkIjoiZDNkZjQ0OGEtMGYyNC00MmMwLWJkMGMtMTBkYjRhYmQzMTg5In0.rJ3lcP6eM7AfG248p9cUqgEWPeFkk7I9K9RAZ7VgdHbAjAOSZcLvzb6mNDqmi3es4B2MuLSPwuxjHFwpgIEbaHWhz-AeWGi9wiqHLYp8HfSD29KwRr899Za_MHotAcOfxTC56aF16GRGbydKC8ldFCKTfu99squm15RcYojfeYbmhnTdOakyeWZs7gPRKOlRuG1eDxNPwFjU65QbbMiejVy-TvcPYHjsW19X2r0USbVNap0YzFPAClrmlntwITpBBoNRSr-9BrwM8zCrmxSx8p-AC44oamJMDSAowCWye7Om29g2Muhh5XjYQoPW9eDbzwH4NqcuI5TISO_xvMy9phdco606a-UDQBGBhwW20gDgeH_MnsHTdxW3NDbGrggLtppJx8EcZ8pjdn1bAmytJAFmYNklTN8iqkKqTTTjX-LkodTNGahWG7XNLKzwjOEL9lr7cCl11jne4TfV3SfJlgtp18eOG4Ck3gXav41djvaRCQxUQ6u9R9LFatN_ITBwQhgl8DlzNMvk3wptvajFbFDuGyl-ccTS-Hjhx3qTpjEHwDuPlzr9QkyOlQSMgEMxeXf4Vee3I_VZJE4_2WWhtYgDiRkiJ7douABr1AS34n5qS6y0vuYsXjrzl3OfH7gSGV3fuhO82erODKS0dqr5K4dAL41O3a02v-UWtcrD_H4"
ENV NUCLIA_KB_ID="903a0322-3d77-4ec3-94fd-3a10021c9500"

# Run the application
CMD ["python", "app.py"]
