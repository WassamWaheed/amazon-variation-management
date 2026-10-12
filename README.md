# Amazon Variation Management

A portfolio reference for planning and auditing Amazon parent/child listing structures.

## Included Files
- [Variation Audit Template](variation_audit_template.csv)
- [Variation Validation Script](variation_check.py)

## Run the Demo

```bash
python variation_check.py variation_audit_template.csv
```

## Variation Planning Checklist
- Confirm that the category supports the intended variation theme
- Keep the parent SKU non-buyable
- Give every child a unique SKU
- Use consistent variation values
- Keep brand/product identity aligned across children
- Review titles and attributes for consistency
- Verify the relationship after upload

## Example Structure

| SKU | Parentage | Parent SKU | Color | Size |
|---|---|---|---|---|
| DEMO-PARENT | parent | — | — | — |
| DEMO-BLK-S | child | DEMO-PARENT | Black | Small |
| DEMO-BLK-M | child | DEMO-PARENT | Black | Medium |

## Troubleshooting
When a variation breaks, inspect both the relationship fields and the underlying catalog attributes. Existing catalog data can conflict with a newly submitted structure.

**Upwork:** https://www.upwork.com/freelancers/~0115a312ed543a19a1
