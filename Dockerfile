FROM python:3
ADD restapi.py /
RUN pip install requests flask python-jenkins atlassian-python-api
EXPOSE 5001
CMD [ "python", "./restapi.py" ]