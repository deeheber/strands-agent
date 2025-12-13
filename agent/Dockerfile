# Build stage
FROM public.ecr.aws/docker/library/python:3.13-slim AS builder

WORKDIR /build

# Copy project configuration and install dependencies
# README.md is required by hatchling build system (referenced in pyproject.toml)
COPY pyproject.toml README.md ./
RUN pip install --no-cache-dir --user .

# Runtime stage
FROM public.ecr.aws/docker/library/python:3.13-slim

WORKDIR /app

# Create non-root user for security
RUN useradd -m -u 1000 bedrock_agentcore

# Copy installed dependencies from builder to bedrock_agentcore user's home directory
COPY --from=builder --chown=bedrock_agentcore:bedrock_agentcore /root/.local /home/bedrock_agentcore/.local

# Set environment variables
# AWS_REGION and AWS_DEFAULT_REGION are set by CDK at runtime
ENV LOG_LEVEL=INFO
ENV PATH=/home/bedrock_agentcore/.local/bin:$PATH
ENV PYTHONPATH=/home/bedrock_agentcore/.local/lib/python3.13/site-packages

# Copy application code
COPY --chown=bedrock_agentcore:bedrock_agentcore src/ .

# Switch to non-root user
USER bedrock_agentcore

# Expose ports
EXPOSE 8080
EXPOSE 8000

# Run the agent
CMD ["python", "agentcore_app.py"]
