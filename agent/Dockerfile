FROM public.ecr.aws/docker/library/python:3.13-slim

WORKDIR /app

# Copy project configuration and install dependencies
COPY pyproject.toml README.md ./
RUN pip install --no-cache-dir .

# Set environment variables
ENV AWS_REGION=us-west-2
ENV AWS_DEFAULT_REGION=us-west-2
ENV LOG_LEVEL=INFO

# Create non-root user for security
RUN useradd -m -u 1000 bedrock_agentcore
USER bedrock_agentcore

# Expose ports
EXPOSE 8080
EXPOSE 8000

# Copy application code
COPY src/ .

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8080/ping')" || exit 1

# Run the agent
CMD ["python", "agentcore_app.py"]
