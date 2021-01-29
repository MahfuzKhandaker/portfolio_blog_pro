# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /portfolio_blog

# Install dependencies
COPY Pipfile Pipfile.lock /portfolio_blog/
RUN pip install pipenv && pipenv install --system

# Copy project
COPY . /portfolio_blog/
