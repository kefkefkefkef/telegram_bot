FROM python:slim
ENV TOKEN='6040946911:AAFkcLOqeDwhisQufRMuQ-4t_XydhZtXRvE'
COPY . .
RUN pip install -r requirements.txt
CMD python bot1.py


