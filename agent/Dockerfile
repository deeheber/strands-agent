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

# Copy installed dependencies from builder
COPY --from=builder /root/.local /root/.local

# Set environment variables
# AWS_REGION and AWS_DEFAULT_REGION are set by CDK at runtime
ENV LOG_LEVEL=INFO
ENV PATH=/root/.local/bin:$PATH
# OpenTelemetry environment variables
ENV OTEL_SERVICE_NAME=strands-agent
ENV OTEL_RESOURCE_ATTRIBUTES=service.name=strands-agent,service.version=0.1.0
ENV OTEL_PROPAGATORS=tracecontext,baggage,xray
ENV OTEL_PYTHON_DISABLED_INSTRUMENTATIONS=urllib3

# Create non-root user for security
RUN useradd -m -u 1000 bedrock_agentcore

# Copy application code
COPY --chown=bedrock_agentcore:bedrock_agentcore src/ .

# Switch to non-root user
USER bedrock_agentcore

# Expose ports
EXPOSE 8080
EXPOSE 8000

# Run the agent
CMD ["python", "agentcore_app.py"]
