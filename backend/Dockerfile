ARG PLONE_VERSION=6.0.0b3
FROM plone/plone-backend:${PLONE_VERSION}

LABEL maintainer="WZ_RS <raphael@wochen-zeitung.ch>" \
      org.label-schema.name="plonedemo-backend" \
      org.label-schema.description="Plone 6 Demo backend image." \
      org.label-schema.vendor="WZ_RS"

# Add local code
COPY . .

# Install local requirements and fix permissions
RUN ./bin/pip install mxdev \
    && mv requirements-docker.txt requirements.txt \
    && ./bin/mxdev -c mx.ini \
    && ./bin/pip install -r requirements-mxdev.txt \
    && chown -R plone: /app
