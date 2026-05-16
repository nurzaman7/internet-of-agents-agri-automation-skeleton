# Deployment

## Local development

```bash
cp .env.example .env
make install
make docker-up
make api
```

In another terminal:

```bash
make edge
```

## Edge deployment

Recommended edge hardware:

- industrial PC for production farms,
- Jetson-class device for image/video processing,
- Raspberry Pi-class device for sensor-only pilots,
- weatherproof enclosure with UPS or solar/battery support.

Deployment steps:

1. Install Docker or Python 3.11.
2. Copy `.env` with cloud endpoint and MQTT credentials.
3. Install only edge dependencies.
4. Run `apps/edge-agent` as a systemd service or container.
5. Test offline mode by disconnecting the network and verifying queue persistence.

## Cloud deployment

The `k8s/` directory contains starter manifests. For production, add:

- managed Postgres,
- managed object storage,
- secrets manager,
- TLS ingress,
- OpenTelemetry collector,
- log retention,
- backup and disaster recovery,
- SSO/OAuth integration,
- network policies,
- per-tenant rate limiting.

## Release gates

Before enabling autonomous actuation:

- run simulation,
- test against a non-production field or bench rig,
- validate emergency stop,
- confirm human approval workflow,
- review audit logs,
- add hardware-specific failure mode tests,
- get local regulatory and operational approvals.
