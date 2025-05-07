# Base: NetBox official image
FROM netboxcommunity/netbox:v4.3-3.3.0 AS production

# Use the built-in NetBox venv
ENV VIRTUAL_ENV=/opt/netbox/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install system dependencies and create fallback pip-compatible venv
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates curl git gnupg python3-dev python3-venv && \
    curl -O https://nginx.org/keys/nginx_signing.key && \
    apt-key add ./nginx_signing.key && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu jammy stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null && \
    apt-get update && \
    apt-get install -y git docker-ce-cli && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    python3 -m venv "$VIRTUAL_ENV" && \
    "$VIRTUAL_ENV/bin/pip" install --upgrade pip setuptools

# Configure NetBox
RUN echo "PLUGINS = ['netbox_netdis']" >> /etc/netbox/config/plugins.py && \
    echo "DEVELOPER = True" >> /etc/netbox/config/configuration.py && \
    pip freeze | grep -i ^django > /tmp/constraints.txt

# Copy and install plugin
COPY pyproject.toml requirements* /opt/code/
COPY ./netbox-plugins/netbox-netdis /opt/code/netbox-plugins/netbox-netdis

RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-compile -c /tmp/constraints.txt \
    --editable /opt/code/netbox-plugins/netbox-netdis

# ---- Dev container stage ----
FROM production AS netbox-dev

ENV HOME=/home
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /opt/code

# Install dev dependencies
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-compile -c /tmp/constraints.txt -r requirements.txt

# Override config for dev use
COPY ./docker/netbox/devcontainer_configuration.py /etc/netbox/config/configuration.py

# Add NetBox SECRET_KEY
RUN python3 /opt/netbox/netbox/generate_secret_key.py | sed 's/^/SECRET_KEY="/;s/$/"/' >> /etc/netbox/config/configuration.py

# Add NetBox to Python path
RUN echo "/opt/netbox/netbox" > "$VIRTUAL_ENV/lib/python3.12/site-packages/netbox.pth"

WORKDIR /opt/netbox/netbox
