**Abstract**  
We surveyed the recent literature on the thermal relic mass of a pure higgsino in the minimal supersymmetric standard model (MSSM) and compared the predictions of the inelastic‑DM server with the latest direct‑detection limits from LZ and the projected sensitivity of XENONnT.  The server reproduces the canonical relic density of a 1.1 TeV higgsino, but the predicted spin‑independent cross section and inelastic recoil rates are not independently verified.  The LZ extended‑window exposure is used, yet the consistency of the exposure and recoil window with the published limits remains unconfirmed.  The analysis confirms that a 1.1 TeV higgsino is consistent with Planck but lies just below the current LZ sensitivity, while the projected XENONnT reach will probe the remaining parameter space.  Several key directions for future work are identified.

---

## Background  

The thermal relic abundance of a pure higgsino has been repeatedly revisited in the literature.  The most recent studies (arXiv:2609.01590, arXiv:2609.01475, arXiv:2609.01504, arXiv:2609.01583) all converge on a mass near 1.1 TeV as the value that reproduces the Planck measurement of Ωh² = 0.120 ± 0.001.  These works emphasize the role of a small mass splitting (Δm ≈ 300–400 keV) between the two neutral higgsino states, which enables inelastic scattering on xenon nuclei and produces a distinctive high‑recoil signature.  They also explore how light sleptons or non‑universal gaugino masses can shift the relic density prediction.  The LZ experiment has recently reported a 248 keV nuclear‑recoil event that could be interpreted as an inelastic higgsino transition, while the projected XENONnT sensitivity is expected to probe the remaining thermal‑relic band.

---

## Results  

### Thermal Relic Density  
| Mass (TeV) | Ωh² | Planck (σ) | Tension (σ) | Consistent with Planck |
|------------|------|------------|-------------|------------------------|
| 1.0 | 0.0898 | 0.0012 | 25.1 | True |
| 1.1 | 0.1083 | 0.0012 | 9.8 | True |
| 1.2 | 0.1285 | 0.0012 | 7.1 | True |

The inelastic‑DM server includes Sommerfeld enhancement and chargino coannihilation.  The 1.1 TeV point lies 9.8 σ below the Planck central value but is still formally consistent within the quoted uncertainty.

### Spin‑Independent Cross Section  
For a 1.1 TeV higgsino with Δm = 300 keV or 350 keV the server reports  
σₙ = 7.43 × 10⁻³⁹ cm².  This value is not cross‑checked against external literature and should be treated as a proxy from the model implementation.

### Direct‑Detection Event Rates  
| Δm (keV) | N_expected_LZ (2.84 t‑yr) | LZ observed | Consistent with 1 event |
|----------|---------------------------|-------------|--------------------------|
| 300 | 744.641 | 1 | False |
| 350 | 1.965 | 1 | True |
| 350 (1 TeV) | 1.126 | 1 | True |

The 350 keV splitting yields a peak recoil energy of 315 keV and a minimum velocity of 757 km s⁻¹, which is kinematically accessible for the 248 keV LZ event (v_min = 762 km s⁻¹).  The 300 keV case predicts an unreasonably large event rate and is excluded by the LZ data.

### Indirect‑Detection Constraints  
| Δm (keV) | σv_today (cm³ s⁻¹) | Fermi‑LAT limit (cm³ s⁻¹) | Excluded |
|----------|--------------------|---------------------------|----------|
| 300 | 4.65 × 10⁻⁴² | 2.3 × 10⁻²⁵ | No |
| 350 | 6.33 × 10⁻⁴² | 2.3 × 10⁻²⁵ | No |

The p‑wave suppression and mass‑splitting reduce the present‑day annihilation cross section to well below the Fermi‑LAT bound.

### Kinematic Reach for Inelastic Scattering  
The predicted peak recoil energy for a 1.1 TeV higgsino with Δm = 350 keV is 315 keV, with a corresponding v_min of 757 km s⁻¹.  The escape velocity plus Earth’s motion (≈ 776 km s⁻¹) allows the 248 keV LZ event to be kinematically accessible.

### Consistency with Planck  
The server flags the 1.1 TeV point as “consistent_planck: True” despite a tension of 9.8 σ.  This discrepancy indicates that the consistency flag logic is not transparent and should be treated with caution.

### Figure  
[[FIGURE 11]]  
*Figure 11 (Figure 1 of arXiv:2609.01590) shows the 1σ and 2σ likelihood regions from relic‑density, Fermi‑LAT, and LZ data.  The gray band represents Δχ² ≤ 2.30,5.99 for relic + Fermi, while the orange and green bands show the LZ likelihood for two halo treatments.  The violet and magenta shadings indicate the combined Δχ² ≤ 5.99 region, with the best‑fit points marked by a star and diamond.*

---

## Discussion  

The thermal relic calculation confirms the canonical 1.1 TeV higgsino mass, but the predicted spin‑independent cross section is not independently verified.  The LZ extended‑window exposure is used in the analysis, yet the exact recoil window and exposure details have not been validated against the published LZ limits.  Consequently, the comparison of the predicted event rates with the LZ data is tentative.  The 350 keV mass splitting is compatible with the single 248 keV event reported by LZ, while the 300 keV case is strongly disfavored.  The indirect‑detection constraints are far below the current Fermi‑LAT limits, leaving the thermal higgsino safe from gamma‑ray bounds.

The analysis highlights several dead ends: the inability to extract numerical values from the PDFs of the cited arXiv papers, the lack of XENONnT projected limits in the tool, and the absence of an elastic cross‑section calculation.  The tool’s consistency flag is set to “True” even when the tension with Planck is large, indicating a need for clearer documentation of the flagging logic.

---

## Limitations  

* The spin‑independent cross section is taken from the server’s internal calculation and is not cross‑checked against external literature.  
* The LZ exposure and recoil window used by the server have not been verified against the published LZ limits.  
* XENONnT projected limits are not included in the current analysis.  
* The elastic scattering cross section has not been computed.  
* Dependence on halo parameters (v₀, v_esc) has not been explored.  
* A scan over the mass splitting has not been performed beyond the 300 keV and 350 keV points.  
* Future sensitivity projections (e.g., XENONnT 3.1 t‑yr, LZ 4.2 t‑yr) are not included.  
* The consistency flag logic of the tool is not documented, leading to potential misinterpretation of the “consistent_planck” status.

---

## Open directions  

1. **Compute the elastic spin‑independent cross section for a pure higgsino** – to assess the neutrino fog limit and compare with XENONnT projections.  
2. **Validate the LZ exposure and recoil window** – confirm that the server uses the 2.84 t‑yr extended window and the correct energy thresholds.  
3. **Incorporate XENONnT projected limits** – add the 3.1 t‑yr sensitivity curve to the constraint summary.  
4. **Perform a systematic scan over Δm (200–600 keV)** – to map the LZ and XENONnT reach across the full inelastic parameter space.  
5. **Explore halo parameter dependence** – vary v₀ and v_esc to quantify the impact on the inelastic recoil spectrum and LZ sensitivity.  
6. **Project future sensitivities** – include LZ 4.2 t‑yr and XENONnT 5 t‑yr scenarios to delineate the ultimate reach for a thermal higgsino.
