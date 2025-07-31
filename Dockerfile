FROM python
RUN apt-get update && \
    apt-get install -y cron && \
    mkdir -p /var/spool/cron/crontabs && \
    touch /var/spool/cron/crontabs/root
RUN apt-get update && apt-get install -y nano
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN playwright install
RUN playwright install-deps  
CMD ["python3", "main.py"]