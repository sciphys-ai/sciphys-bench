# XRD evaluation track

The XRD track is the first reference design for evaluating parser behavior, phase evidence, quantitative analysis, agent decisions, and claim integrity.

Proposed public real-data strata include single phase, mixtures, trace impurities, preferred orientation, substrate peaks, fluorescence/background, low signal-to-noise, broad/nanocrystalline peaks, amorphous content, wavelength variation, and vendor-format variants. Each stratum needs sufficient independent samples to report uncertainty and cannot be represented by one demonstration file.

Core outputs include parse diagnostics, normalized measurement, detected peaks with parameters, ranked candidates and alternatives, unmatched observations, missing strong references, fit/residual artifacts where applicable, uncertainty, limitations, and an Evidence Bundle.

Synthetic cases in `sciphys-os` are currently regression fixtures only. This track must not make real-world accuracy claims until licensed external measurements are frozen, expert reviewed, and released with reproducible baselines.
