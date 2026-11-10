# Class 11 — Network Inventory Audit

## Context

This project is part of **Class 11 — Tuples and Sets**.

The goal is to apply the Python concepts learned so far by building a small network inventory auditing tool.

## Project Description

Imagine you are working as a Network Engineer and receive an inventory of network devices.

You must develop a program capable of detecting:

- Duplicate management IP addresses.
- Unauthorized VLANs.
- Required VLANs missing from individual devices.
- Duplicate VLANs within a device configuration.
- VLANs used across the entire infrastructure.
- VLANs shared between different locations.

The program must generate a structured **network audit report**.

### Initial Data

```python
# (hostname, management_ip, location, vlans)

inventory = [
    ("R1", "192.168.1.1", "HQ", (10, 20, 30)),
    ("SW1", "192.168.1.2", "HQ", (10, 20, 40, 40)),
    ("SW2", "192.168.1.2", "Branch", (10, 50, 99)),
    ("R2", "192.168.1.4", "Branch", (10, 20, 50)),
    ("SW3", "192.168.1.5", "HQ", (10, 30, 60)),
]

approved_vlans = {10, 20, 30, 40, 50}
required_vlans = {10, 20}
```

## Project Tasks and Git Workflow

The project is divided into **four parts**. Each part will be developed and recorded in a separate Git commit to document the development process step by step.

### Part A — Management IP Audit

- Identify duplicate management IP addresses.
- Determine which devices share each duplicated IP.
- Calculate the number of unique management IP addresses.
- Preserve the original inventory.

> **Commit 1:** Management IP audit.

### Part B — Individual VLAN Audit

For each network device:

- Detect duplicate VLANs within its configuration.
- Identify unauthorized VLANs.
- Identify missing required VLANs.
- Use a flag to indicate whether the device has any issues.

> **Commit 2:** Individual VLAN audit.

### Part C — Network-Wide VLAN Audit

Calculate:

- All VLANs used across the infrastructure.
- Approved VLANs currently in use.
- Unauthorized VLANs.
- Approved VLANs not currently in use.

Use set operations to perform these comparisons.

> **Commit 3:** Network-wide VLAN audit.

### Part D — Location Comparison and Final Report

Separate the VLANs used in each location:

- HQ
- Branch

Identify:

- VLANs shared between both locations.
- VLANs used only in HQ.
- VLANs used only in Branch.

Generate the final network inventory audit report.

> **Commit 4:** Location comparison and final audit report.

## Python Concepts and Requirements

Apply the concepts learned up to Class 11:

| Element | Purpose |
|---|---|
| Lists | Store inventory and results |
| Tuples | Represent devices and their VLAN configurations |
| Sets | Handle duplicates and compare VLANs |
| Strings | Store hostnames, IP addresses and locations |
| `for` | Iterate through devices and VLANs |
| `if / else` | Evaluate conditions and detect issues |
| `in` | Check membership |
| `len()` | Calculate quantities |
| Flags | Track detected issues |
| `append()` | Store results |
| `add()` / `update()` | Build sets |
| `set()` | Convert collections and eliminate duplicates |

### Restrictions

- Do not use **dictionaries** (Class 12).
- Do not use external libraries.
- Do not use **functions (`def`)**.
- Do not modify tuples directly.
- Do not remove devices from the original inventory.
- Do not simply print results: store the necessary data to generate the final report.

## Expected Output

The program should generate a structured report similar to the following:

```text
NETWORK INVENTORY AUDIT

1. DEVICE INVENTORY
- Total devices: ...
- Unique management IPs: ...
- Duplicate management IPs: ...

2. DEVICE AUDIT
- Device: R1
- Duplicate VLANs: ...
- Unauthorized VLANs: ...
- Missing required VLANs: ...
- Status: ...

3. NETWORK-WIDE VLAN AUDIT
- VLANs in use: ...
- Approved VLANs in use: ...
- Unauthorized VLANs: ...
- Approved VLANs not in use: ...

4. LOCATION COMPARISON
- HQ VLANs: ...
- Branch VLANs: ...
- Shared VLANs: ...
- HQ only: ...
- Branch only: ...

5. FINAL STATUS
- Devices with issues: ...
- Total devices audited: ...
- Overall result: ...
```

## How to Run

```bash
python Network-Inventory-Audit.py
```

## Project Status

**Exercise in progress.**