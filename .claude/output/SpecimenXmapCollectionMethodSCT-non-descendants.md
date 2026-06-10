# SpecimenXmapCollectionMethodSCT — non-descendants of `<<17636008 |Specimen collection (procedure)|`

Source: `~/Downloads/SpecimenXmapCollectionMethodSCT.xlsx`
SNOMED CT edition: `SnomedCT_ManagedServiceUS_PRODUCTION_US1000124_20260301T120000Z` (US Edition, 2026-03-01)
Root: `17636008 |Specimen collection (procedure)|` (139 concepts in `<<17636008`, inclusive)

## Summary

| Bucket | Count |
|---|---|
| Rows in spreadsheet | 94 |
| Rows that ARE descendants of `<<17636008` | 25 |
| Rows that are NOT descendants of `<<17636008` | **69** |
| &nbsp;&nbsp;&nbsp;&nbsp;— Inactive in this SNOMED edition | 6 |
| &nbsp;&nbsp;&nbsp;&nbsp;— Active but not in the `<<17636008` subhierarchy | 63 |
| Duplicate rows in the source spreadsheet | 3 |
| Non-procedure semantic-tag concepts | 2 |

## Inactive concepts (6)

These are retired in the 2026-03-01 US Edition snapshot.

| Code | Description in spreadsheet |
|---|---|
| 24139008 | Endoscopy of urinary bladder (procedure) |
| 176178006 | Diagnostic cystoscopy (procedure) |
| 397394009 | Bronchoalveolar lavage (procedure) |
| 1388791008 | Urine collection after prostatic massage (procedure) |
| 1571000284107 | Arterial sampling catheter procedure (procedure) |
| 78181000284104 | Cornea impression (procedure) |

## Active concepts that are NOT descendants of `<<17636008` (63 unique)

Mostly biopsies, irrigations / lavages, drainage, aspirations of body sites, excisions, and other procedures that *produce* a specimen as a side effect but live elsewhere in the procedure hierarchy.

| Code | Description |
|---|---|
| 6853008 | Nasogastric tube aspiration (procedure) |
| 14766002 | Aspiration (procedure) |
| 24619005 | Skin scraping for examination (procedure) |
| 29240004 | Autopsy |
| 32218000 | Biopsy of esophagus (procedure) |
| 32534001 | Biopsy of spleen (procedure) |
| 36213007 | Endoscopy and brush biopsy (procedure) |
| 44414004 | Aspiration of Bartholin's cyst (procedure) |
| 48635004 | Fine needle biopsy (procedure) |
| 49401003 | Bone marrow aspiration procedure (procedure) |
| 54133007 | Biopsy of spermatic cord (procedure) |
| 54535009 | Cone biopsy of cervix (procedure) |
| 56757003 | Scraping (procedure) |
| 63293007 | Fine needle biopsy of seminal vesicle (procedure) |
| 64663002 | Prostatic massage (procedure) |
| 67889009 | Irrigation (procedure) |
| 68688001 | Curettage (procedure) |
| 70163005 | Excision of ganglion cyst (procedure) |
| 75016008 | Biopsy of soft tissue (procedure) |
| 78533007 | Irrigation of urinary bladder (procedure) |
| 79121003 | Biopsy of stomach (procedure) |
| 80657008 | Bronchoscopy with brush biopsy (procedure) |
| 81723002 | Amputation (procedure) |
| 83152002 | Oophorectomy (procedure) |
| 86273004 | Biopsy (procedure) |
| 89305009 | Abdominal paracentesis (procedure) |
| 91602002 | Thoracentesis (procedure) |
| 122462000 | Drainage procedure (procedure) |
| 129112001 | Aspiration from trachea (procedure) |
| 168461002 | Postmortem examination (procedure) |
| 173830003 | Gastric lavage (procedure) |
| 175189006 | Pericardial biopsy (procedure) |
| 176747002 | Aspiration of pouch of Douglas (procedure) |
| 177788009 | Open drainage of pleural cavity (procedure) |
| 178263003 | Biopsy of muscle (procedure) |
| 232595000 | Bronchoscopic lavage (procedure) |
| 234319005 | Splenectomy (procedure) |
| 235157009 | Endoscopic brushings of gastrointestinal tract (procedure) |
| 236880008 | Curettage of uterus and endometrial sampling (procedure) |
| 236886002 | Hysterectomy (procedure) |
| 240977001 | Biopsy of skin (procedure) |
| 243763007 | Venous sampling catheter procedure (procedure) |
| 258429002 | Rectal scrape specimen (specimen) |
| 261665006 | Unknown (qualifier value) |
| 277762005 | Lumbar puncture (procedure) |
| 287571005 | Diagnostic bronchial aspiration (procedure) |
| 299693003 | Biopsy of jejunum (procedure) |
| 303995001 | Buccal smear procedure (procedure) |
| 386802000 | Endometrial biopsy (procedure) |
| 387715005 | Peritoneal lavage (procedure) |
| 410729004 | Amniocentesis (procedure) |
| 416107004 | Cervical cytology test (procedure) |
| 430111007 | Fine needle aspiration biopsy of spermatic cord (procedure) |
| 430854000 | Touch preparation of specimen (procedure) |
| 439336003 | Brush biopsy (procedure) |
| 446847002 | Drainage of pleural cavity via chest tube (procedure) |
| 446860008 | Collection of cerebrospinal fluid via ventriculoperitoneal shunt (procedure) |
| 447097009 | Scraping of nail (procedure) |
| 448895004 | Sampling for smear (procedure) |
| 697972001 | Cutting of hair (procedure) |

## Concepts with non-procedure semantic tag (preferred names from US Edition)

| Code | Preferred name (en-US PT) | FSN |
|---|---|---|
| 258429002 | Rectal scrape specimen | Rectal scrape specimen *(specimen)* |
| 261665006 | Unknown | Unknown *(qualifier value)* |

These do not belong in a `Specimen.collection.method` value set — `258429002` is a specimen and `261665006` is a generic "Unknown" qualifier.

## Duplicate rows in the source spreadsheet (preferred names from US Edition)

| Code | Preferred name (en-US PT) | FSN | Notes |
|---|---|---|---|
| 122462000 | Drainage procedure | Drainage procedure *(procedure)* | Listed twice with same description |
| 14766002 | Aspiration | Aspiration *(procedure)* | Listed twice with same description |
| 232595000 | Bronchoscopic lavage | Bronchoscopic lavage *(procedure)* | Listed once as "Bronchoscopic irrigation" and once as "Bronchoscopic lavage"; both are active terms on the same concept, but **Bronchoscopic lavage** is the en-US PT |
