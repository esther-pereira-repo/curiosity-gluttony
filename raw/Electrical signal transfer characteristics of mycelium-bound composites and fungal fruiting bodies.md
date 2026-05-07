---
title: "Electrical signal transfer characteristics of mycelium-bound composites and fungal fruiting bodies"
source: "https://www.sciencedirect.com/science/article/pii/S1754504824000291"
author:
  - "[[AbstractMycelium-bound composites are normally made of discrete lignocellulosic substrate elements bound together by filamentous fungal hyphae. They can be formed into bespoke components of desired geometries by moulding or extrusion. Mycelium-bound composites with live fungi have been shown to be electrically conductive with memfractive and capacitive attributes. They can be integrated into electrical circuits with nonlinear electrical properties. Advancing fungal electronics]]"
  - "[[we studied the AC conductive properties of mycelium-bound composites and fungal fruit bodies at higher frequencies across three overlapping bands; 20 Hz to 300 kHz]]"
  - "[[10 Hz to 4 MHz and 50 kHz to 3 GHz. Measurements indicate that mycelium-bound composites typically act as low-pass filters with a mean cut-off frequency of ∼500 kHz; with ∼−14 dB/decade roll-off]]"
  - "[[and mean attenuation across the pass band of <<math><mo is=\"true\">&lt;</mo></math>1 dB. Fruiting bodies have between one or two orders of magnitude lower mean cut-off frequency (5 kHz–50 kHz depending on species); with −20 dB/decade to −30 dB/decade roll-off]]"
  - "[[and mean attenuation across the pass band of <<math><mo is=\"true\">&lt;</mo></math>3 dB. The mechanism for the frequency-dependent attenuation is uncertain; however]]"
  - "[[the high water content]]"
  - "[[which is electrically conductive due to dissolved ionisable solids is probably a key factor. The potential for mycelium-bound composites and fruiting bodies in analog computing is explored.]]"
  - "[[Roshan Weerasekera a b]]"
  - "[[Andrew Adamatzky a]]"
published:
created: 2026-05-07
description: "Mycelium-bound composites are normally made of discrete lignocellulosic substrate elements bound together by filamentous fungal hyphae. They can be fo…"
tags:
  - "clippings"
---
[https://doi.org/10.1016/j.funeco.2024.101358](https://doi.org/10.1016/j.funeco.2024.101358 "Persistent link using digital object identifier")

Under a Creative Commons [license](http://creativecommons.org/licenses/by/4.0/)

Open access

## Keywords

Mycelium

Hypha

Analog

Unconventional

Edge

Biohybrid

## 1\. Introduction

In recent years, fungal research and biotechnology have been on the rise, going beyond the traditional roles of fungi in ecosystems, namely decomposition, parasitism, and symbiosis. Researchers from various fields worldwide have come to realise the incredible potential that lies within the vast world of fungi, often described as the ‘mycological iceberg’, which is estimated to encompass around 3.8 million species (), of which only a fraction have been thoroughly explored. This growing interest for fungi highlights the importance of understanding their intrinsic [electrical activity](https://www.sciencedirect.com/topics/immunology-and-microbiology/electric-activity) as a means to unravel the mysteries of these fascinating and omnipresent organisms. Fungal [electrophysiology](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/electrophysiology), aided by advances in machine learning and AI-driven data analysis, is emerging as an exciting and promising field, poised to uncover profound insights into the fungal kingdom ().

The first evidence of action potential-like spiking activity in fungi was discovered in 1976 (), and it was confirmed in 1995 (; ). Techniques for recording and analysing electrical activity in fungi [fruiting bodies](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/fruiting-body) and colonised substrates were developed (; ). These breakthroughs have paved the way for a better understanding of electrical signal transfer in natural fungal networks and systems. Understanding the mechanisms underlying electrical communication in fungi is critical to understanding their role in ecological processes. For example, studies have discovered that the fungus [Pleurotus djamor](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/pleurotus-djamor) shows trains of electrical [potential spikes](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/spike-potential) that looked like the action potential spikes exhibited by animal [nervous systems](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/nervous-system) (). These spikes of electrical potentials have been observed and corroborated in many other species ( have been hypothesised to represent signaling for [mycelium](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/mycelium) propagation in the substrate, nutrient and metabolite transport, and [mycelium](https://www.sciencedirect.com/topics/immunology-and-microbiology/mycelium) network communication processes ().

The integration of newly obtained knowledge from the fields of bioelectronics, [synthetic biology](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/synthetic-biology), and electro-microbiology enables the use of organisms as electrical elements inside electronic circuits (;;; ). The unique characteristics of ‘living’ electronics have the potential to benefit several cross-disciplinary applications, including sensing, energy conversion, and hybrid information processing. The integration of neurons and electronic components, such as the construction of neuroelectronic junctions and [neural networks](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/neural-network) (), is expected to propel advances in computing. Furthermore, bioelectronics exhibit enhanced environmental [sustainability](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/environmental-impact-assessment) as a result of their minimal energy use and the ability to recycle them at the end of their lifespan (;; ). Fungi are promising at this regard due to their adaptability and resilience when compared to other organisms ().

The study of fungal electronics has the potential to provide valuable insights into the intricate mechanisms of electrical signal transfer in natural fungal networks and systems (). By manipulating and studying the electrical and biological properties () of fungal highways, researchers can explore important processes (). For example, investigating the role of electrical impulses in the chemotaxis of fungal networks could provide significant insights into the navigation and survival mechanisms used by fungi (). Moreover, the investigation of engineered fungal systems may provide insights into the function of communication within indigenous fungal networks seen in nature (). Directed [genetic](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/genetics) modifications could potentially enhance the electrophysiological properties of fungi, thereby facilitating in-depth exploration of electrical signal propagation through mycelial networks, a cornerstone in the development of organic bioelectronic devices (). The tantalising potential of using fungi for memory and data storage could also be realised through precise genetic engineering, allowing the encoding, storage, and retrieval of electrical signals within fungal networks, a concept integral to electrophysiological and bioelectronical research (). Moreover, the biosynthetic capacities of fungi could be also harnessed through genetic engineering to yield novel [conductive materials](https://www.sciencedirect.com/topics/materials-science/conductive-material), thereby broadening the palette of tools available for electrophysiological investigations. Unlike the crude control rendered by non-genetic tools, genetic engineering, especially with standardised toolsets like FungalBraid (; ), provides the finesse and precision indispensable for in-depth electrophysiological studies, propelling us closer to innovative bio-computational systems and memory storage solutions grounded in [electrophysiology](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/electrophysiology).

Some of the recent research on fungal electronics has been propelled by the development of mycelium-based biomaterials such as self-standing mycelium-bound composites and flexible fungal skins (; ). Mycelium-bound composites are typically masses of organic substrates (e.g. straw, shives, woodchips, sawdust, or seeds) colonised and bound together by hyphae (;;; ). These can be formed into custom geometries of desired shape and size by moulding () or extrusion (). Mycelium-bound composites might be grown to fabricate monolithic circuits (e.g. mycelium networks ()). In () we proposed developing a [functional material](https://www.sciencedirect.com/topics/materials-science/functional-material) by using live fungal mycelium, functionalising the substrate with [nanoparticles](https://www.sciencedirect.com/topics/materials-science/nanoparticle) and polymers to make mycelium-based electronics.

Mycelium-bound composites and fungal [fruiting bodies](https://www.sciencedirect.com/topics/immunology-and-microbiology/fruiting-body) have been shown to have complex electrical properties at lower frequencies including resistive spikes (), mem-fractive (exhibiting a combination of passive memory) (; ) and modify frequencies of external electrical inputs (). Electrical properties are affected by [moisture content](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/moisture) (). They are also known to respond to chemical and physical stimuli by changing patterns of their electrical activity (;;;; ) and [electrical conductivity](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/electric-conductivity) (). In () we proposed a novel technological direction – fungal electronics. Fungal electronics is a family of living electronic devices made of mycelium-based biomaterials. Fungal electronic devices are capable of changing their impedance and generating spikes of electrical potential in response to external control parameters. The intrinsic biocompatible of fungal electronics electronic simplifies interfacing with biological systems. For example, fungal electronics can be embedded into fungal materials and wearables or used as stand alone sensing and computing devices. Furthermore, the flexibility of fungal electronics allows for the creation of devices with curved and non-planar shapes. This adaptability is aided by their distinct mycelium architecture, which allows for the growth of fungal electronics on a variety of substrates. Fungi can repair damage through their natural growth and regeneration processes, so fungal electronics have the potential to be self-healing (;;;;;;;; ). Fungal electronics also have the ability to biodegrade, making them an environmentally friendly option for the management of electronic waste (;; ).

Elementary fungal-electronic components must communicate with each other. One of the ways to transmit information in a fault-tolerant manner is to encode it in frequencies of [alternating current](https://www.sciencedirect.com/topics/immunology-and-microbiology/alternating-current) (AC). As part of our research into the information-transmissive properties of mycelium-bonded composites and fruiting bodies, we decided to study how their electrical properties change across the higher frequency spectrum (; ).

Furthermore, given that ecosystems are complex and dynamic system (), we believe that monitoring the electrical activity of its fungal networks can provide valuable insights into the underlying metabolic processes that drive ecosystem functioning, allowing us to better understand the interactions that occur. For example, obtaining information on ecosystem health could have significant implications for future AI-controlled farming operations and restoration efforts (). Microbe activity, in particular, is critical to the functioning of biogeochemical systems because it influences key ecosystem processes such as nutrient cycling and organic matter breakdown (). Measuring [microbial activity](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/microbial-activity) through electrical activity, in this case fungi, can serve as a useful biomarker of exposure in a variety of environments, providing insight into changes or disruptions in these ecosystem processes.

A compelling illustration of the ecological significance of fungal electrical activity was presented in Fukasawa et al.’s work (). Through field experiments that involved measuring extracellular electrical activities in [Laccaria](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/laccaria) bicolor, they demonstrated that fungi exhibit reduced electrical activity in relatively dry conditions. On the contrary, following rainfall, the amplitudes of fungal electrical oscillations exhibited a substantial increase, frequently exceeding 100 mV. Additionally, the study by Fukasawa et al. () provided evidence of electrical [signal transmission](https://www.sciencedirect.com/topics/immunology-and-microbiology/signal-transduction) between neighbouring fruit bodies.

This evidence shows that understanding the electrical activity of fungi is crucial for analysing their [physiological state](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/physiological-state) in ecological contexts for several reasons.
- ●
	Indicator of Vitality: Electrical activity is often a sign of life in organisms. In the case of fungi, monitoring their electrical activity can help determine whether they are alive and metabolically active, providing information about their overall health and vitality.
- ●
	Response to Environmental Stimuli: Fungi, like all living organisms, respond to their environment. Changes in electrical activity can serve as indicators of how fungi react to external factors such as temperature, humidity, light, and the presence of other organisms. This information can help researchers understand the [ecological niches](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/ecological-niche) in which fungi thrive.
- ●
	[Symbiotic Relationships](https://www.sciencedirect.com/topics/immunology-and-microbiology/symbiotic-relationship): Fungi have various symbiotic relationships with plants, animals, and other fungi. Understanding their electrical activity can shed light on the nature of these interactions. For example, [mycorrhizal fungi](https://www.sciencedirect.com/topics/immunology-and-microbiology/mycorrhiza) form symbiotic relationships with plants and exchange nutrients. Monitoring electrical activity can reveal how this exchange occurs and whether it benefits both parties.
- ●
	Bioindicators: Fungi are essential components of ecosystems and can be bioindicators of [environmental health](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/environmental-health). Changes in their electrical activity may indicate pollution, habitat degradation, or other ecological disturbances. Studying fungal electrical activity can help monitor the overall well-being of an ecosystem.
- ●
	[Biogeochemical Cycling](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/biogeochemical-cycling): Fungi play a vital role in nutrient cycling, particularly in decomposition and nutrient release. Understanding their electrical activity can provide insights into how fungi contribute to these processes and influence nutrient availability in ecosystems.
- ●
	Ecological Functions: Fungi contribute to the ecological functioning of ecosystems by breaking down organic matter, facilitating nutrient cycling, and interacting with other organisms. Their electrical activity can reveal to what extent they perform these ecological functions and how they can respond to changing environmental conditions.
- ●
	Conservation and Restoration: Monitoring the electrical activity of fungi can be useful in conservation efforts. It can help assess the health of fungal populations in threatened ecosystems and guide restoration strategies to ensure their continued ecological functions.
In summary, studying the electrical activity of fungi is a valuable tool for [ecologists](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/ecologist) because it provides insights into the physiological state of fungi, their responses to the environment, and their roles in ecosystems. This knowledge contributes to a deeper understanding of ecological [dynamics](https://www.sciencedirect.com/topics/immunology-and-microbiology/dynamics) and the [conservation of biodiversity](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/conservation-of-biodiversity).

The objectives of this study are: to clarify the frequency-dependent electrical attenuation of mycelium-bound composites and fruiting bodies, explore their potential for nonlinear electrical elements in analog computing, and improve understanding of ecosystem functioning through knowledge of their electrical properties.

## 2\. Methods and materials

### 2.1. Living fungal materials

Five species of fresh [fruiting bodies](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/fruiting-body) were sourced from a local supplier (Wholesale Fruit Centre Bristol, UK), see A, B, C, D, E. Two additional species were obtained from a forest mushroom farm (Livesey Brothers Ltd, Leicestershire, UK), see F, G. The fungal [fruiting bodies](https://www.sciencedirect.com/topics/immunology-and-microbiology/fruiting-body) were kept at room temperature (18 °C–22 °C) and initial measurements made within 8 h of purchase.

![Fig. 1](https://ars.els-cdn.com/content/image/1-s2.0-S1754504824000291-gr1.jpg)

Download: Download high-res image (1MB)

A 100 g block of substrate (Rye [grain](https://www.sciencedirect.com/topics/food-science/cereal) seeds) well colonised with the fungus [Pleurotus ostreatus](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/pleurotus-ostreatus) (Ann Miller's Speciality Mushrooms, UK, ()) was enclosed in [polypropylene](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/polypropylene) bags fitted with a 0.5 μm air filter patch, see A. The block was kept at room temperature (18 °C–22 °C) inside a growth tent (in darkness) when not being used in experiments.

![Fig. 2](https://ars.els-cdn.com/content/image/1-s2.0-S1754504824000291-gr2.jpg)

Download: Download high-res image (580KB)

The [moisture content](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/moisture) of mycelium-bound substrates and fruiting bodies was determined by the following procedure: (1) measure the ‘wet’ weight of the sample (2) dehydrate the sample in an oven at 80 °C for ∼ 48 h (3) measure the ‘dry’ weight of the sample (4) calculate the difference between ‘wet’ and ‘dry’ weights then dividing by the ‘dry’ weight.

### 2.2. Impedance of mycelium-bound composites and fungal fruiting bodies over the 20 Hz to 300 kHz frequency range

To make electrical connections to the mycelium-bound composites and fungal fruiting bodies, bespoke electrodes were developed. The copper crimps at the terminal end of platinum [iridium](https://www.sciencedirect.com/topics/materials-science/iridium) [needle electrodes](https://www.sciencedirect.com/topics/materials-science/needle-electrode) (Technomed Ltd, UK) were soldered to the centre conductor of SMA (SubMiniature version A) right angle connectors, see C. The needles were inserted ∼15 mm depth into body of grain spawn (see A) and through fungal fruiting bodies of various thicknesses (see B). The distance between the centres of the needle electrodes was maintained at 20 mm by a spacer, see B. ‘Radial’ measurements were recorded with the electrodes equal distance from the centre of the cap of the fruiting body (see E) while ‘axial’ measurements were recorded with the electrodes perpendicular to centre of the cap. ‘Radial’ electrodes are therefore across the cap's gills while ‘axial’ electrodes are aligned with the gills (see D).

Measurements were recorded within a bespoke RF-shielded test chamber, see. The mycelium-bound composite and fruiting bodies were electrically insulated (and physically separated by ∼5 mm) from the inside of diecast [aluminium](https://www.sciencedirect.com/topics/materials-science/aluminum) enclosure (model Hammond 1550H, 222 mm × 146 mm x 105 mm) with a [polypropylene](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/polypropylene) liner. Coaxial leads and connectors (including through the RF-chamber wall) were SMA type.

[Electrical impedance](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/electrical-impedance) and other circuit parameters were measured using a digital Inductance Capacitance Resistance (LCR) meter (model 891, BK Precision Ltd, UK ()). The LCR meter was configured to scan across the 20 Hz to 300 kHz frequency range applying 1 V <sub><em>rms</em></sub> sinusoidal voltage waveform through the [mycelium](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/mycelium) bound composite and fruiting bodies. 301 measurements being automatically recorded per sweep with ∼0.05 % accuracy.

### 2.3. Signal propagation in mycelium bound composites and fungal fruiting bodies over the 10 Hz to 4 MHz frequency range

The signal propagation was measured using an impedance – amplitude – phase frequency response network analyzer (C60, Cypher Instruments, [London](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/london), UK ()). The C60 network analyser passes 2 V <sub><em>pp</em></sub> sinusoidal voltage waveform through the [mycelium](https://www.sciencedirect.com/topics/immunology-and-microbiology/mycelium) bound composite and fruiting bodies at a plurality of frequencies (10 Hz–4 MHz). The network analyser was connected to the native CypherGrapgh (V1.28) software package on a Windows computer to control functionality and store measurements. The software evaluates the waveform after it passes through the sample and displays it as a Bode plot, the frequency response was analysed and measurements stored.

Experimental ‘controls’ were recorded using the same setup, however, the mycelium-bound composite was replaced with; uncolonised substrate (Rye grain seeds in 50 ml glass beaker) and electrically insulating substrate (open cell [polyurethane](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/polyurethan) foam with water of different conductivity in 50 ml glass beaker). The ‘controls’ were subject to the same frequency spectrum of sinusoidal waveforms to explore if part of the signal was being propagated through the fungal hypha rather than the substrate or the instrumentation.

### 2.4. Exemplar recordings of S-parameters in mycelium bound composites and fungal fruiting bodies over the 50 kHz to 3 GHz frequency range

S-parameters S11 and S21 were measured using the previously described setup of electrodes and RF-shielded test chamber. This allowed reflection and transmission measurements. The signal propagation was measured using a Vector Network Analyser (NanoVNA-F V2, [Amazon](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/amazon) Plc, UK ()). The instrument's maximum output power depends on the frequency and is between −14 dB m to −19 dB m. The dynamic range for reflection measurements (S11) is 70 dB or better up to 1.5 GHz and 60 dB or better up to 1.5 GHz–3 GHz.

The Vector Network Analyser (VNA) was regularly calibrated to maintain accuracy involving short-circuit, 50 Ω load, and open termination, followed by a direct connection between ports (inside the RF-chamber). VNA was connected to the native NanoVNA-QT VNA Saver (V 0.5.3) software package on a Windows computer to control functionality and store measurements.

## 3\. Results

### 3.1. Impedance of mycelium-bound composites and fungal fruiting bodies over the 20 Hz to 300 kHz frequency range

The LCR meter used in this experiment fits a parallel model (*R* <sub><em>p</em></sub> *C* <sub><em>p</em></sub>) for low [capacitance measurement](https://www.sciencedirect.com/topics/materials-science/capacitance-measurement) and series model (*R* <sub><em>s</em></sub> *C* <sub><em>s</em></sub>) for high capacitance measurement. Since the capacitance of the mycelium is high, it has fitted a series RC network as shown with series resistance (*R*) and a series capacitance (*C* <sub><em>s</em></sub>). The reason being if the capacitance is small, the parallel resistance becomes large and more relevant than the series resistance. If the capacitance is large, the series resistance becomes dominant and the parallel resistance becomes insignificant.

![Fig. 3](https://ars.els-cdn.com/content/image/1-s2.0-S1754504824000291-gr3.jpg)

Download: Download high-res image (94KB)

The [electrical impedance](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/electrical-impedance) $Z \left(\right. f \left.\right) = R + \frac{1}{j \omega C_{s}}$ of the fruiting body (cap and stalk) decreased with increasing frequency over 20 Hz to 300 kHz range. The impedance of mycelium-bound composite also decreased but at a considerably slower rate, see. The stalk of the fruiting body has a higher [electrical impedance](https://www.sciencedirect.com/topics/materials-science/electrical-impedance) than the cap. The axial impedance of cap is lower than the radial impedance at lower frequencies becoming similar ∼300 kHz. This trend shows that mycelium-bound composites demonstrate lower impedance at higher frequencies.

![Fig. 4](https://ars.els-cdn.com/content/image/1-s2.0-S1754504824000291-gr4.jpg)

Download: Download high-res image (367KB)

A summary of other electrical properties of mycelium-bound composites and fungal fruiting bodies is shown in. The fruiting body's stalk has less than half the capacitance, more than twice the inductance, and lower steady-state DC resistance of the cap (both radial and axial). The steady-state DC resistance of the colonised substrate is higher than the fruiting body.

Table 1. Electrical properties of the fruiting bodies of Agaricus bisporus and colonised substrate at 300 kHz.

<table><thead><tr><td rowspan="3">Empty Cell</td><th colspan="3">Fruiting body</th><th rowspan="3">Colonised substrate body</th></tr><tr><th colspan="2">cap</th><th>stalk</th></tr><tr><th>radial</th><th>axial</th><th>radial</th></tr></thead><tbody><tr><td>R (kΩ)</td><td>1.991</td><td>1.782</td><td>4.438</td><td>8.312</td></tr><tr><td>Cs (pF)</td><td>348</td><td>394</td><td>156</td><td>551</td></tr><tr><td>Z (kΩ)</td><td>2.490</td><td>2.230</td><td>5.580</td><td>8.390</td></tr></tbody></table>

Using the lump model of the fruiting body and the colonised substrate, we have carried out SPICE S-parameter simulation to understand the frequency dependant characteristics of the mycelium substrate for signal transfer characteristics. depict the S-parameter simulation of the lump model for the return loss (S11) and the gain (S21) for different cases. In very low frequencies up to 100 kHz, a significant amount of the signal is reflected back to the source and the amount of signal transferred through the substrate is very low. However, starting from around 1 MHz onward the return loss becomes negative around −0.1 to −0.5 which is still higher in comparison to a normal semi-conductive substrates such as [silicon](https://www.sciencedirect.com/topics/materials-science/silicon).

![Fig. 5](https://ars.els-cdn.com/content/image/1-s2.0-S1754504824000291-gr5.jpg)

Download: Download high-res image (406KB)

### 3.2. Signal propagation in mycelium-bound composites and fungal fruiting bodies over the 10 Hz to 4 MHz frequency range

The signal propagation passing through mycelium-bound composite was frequency dependent; the lower frequency waveforms passed through with little attenuation while the higher frequencies became increasingly attenuated. The magnitude frequency profile matched that of a low pass filter; the phase response also appeared to correlate with a typical low pass filter. The Bode plot of mycelium-bound composite, see, shows the level of attenuation increased noticeably above 100 kHz (e.g. −8 dB at 1 MHz). The phase decreases noticeably above 10 kHz.

![Fig. 6](https://ars.els-cdn.com/content/image/1-s2.0-S1754504824000291-gr6.jpg)

Download: Download high-res image (440KB)

The Bode plots of five species of fungal fruiting bodies are shown in. For measurement consistency, the electrodes (with 20 mm spacing) were normally inserted into the caps of the fruiting bodies. However, the smaller physical size of *[Hypsizygus](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/hypsizygus "Learn more about Hypsizygus from ScienceDirect's AI-generated Topic Pages")* *tessellatus* meant that in one recording both electrodes were inserted into the stalk, and for a second recording one electrode was in the stalk and one in the cap. The mean cut-off frequency was between 5 kHz and 50 kHz (depending on species); −20 dB/decade to −30 dB/decade roll-off, with mean attenuation across the pass band of ∼−3 dB.

![Fig. 7](https://ars.els-cdn.com/content/image/1-s2.0-S1754504824000291-gr7.jpg)

Download: Download high-res image (706KB)

To support the analysis [of material properties](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/property-of-materials) (attenuation and phase against frequency) six configurations were measured; well colonised substrate ([Pleurotus ostreatus](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/pleurotus-ostreatus) on Rye seeds, blocks of 100 g and 750 g), uncolonised substrate (Rye seeds ∼66 % moisture content and Rye seeds with 2 ml of mains water 0.0025 MΩ cm added to increase moisture content to ∼76 %, in 50 ml glass beakers) and open cell [polyurethane foam](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/polyurethane-foam) sponge (with 2 ml de-ionised water 10 MΩ cm and 2 ml mains water 0.0025 MΩ cm, in 50 ml glass beakers), see.

![Fig. 8](https://ars.els-cdn.com/content/image/1-s2.0-S1754504824000291-gr8.jpg)

Download: Download high-res image (750KB)

It was observed during measurements that the cap and stalk of fruiting bodies can have significantly different electrical properties. By way of example, shows an exemplar of sequential recording from the same [Agaricus bisporus](https://www.sciencedirect.com/topics/immunology-and-microbiology/agaricus-bisporus) fruiting body. Organic materials can exhibit electrical phase changes at kHz frequencies. These changes are a result of the energy absorbed from an applied [electromagnetic field](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/electromagnetic-field), which leads to molecular rearrangements and altered physical properties such as [dielectric constant](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/dielectric-constant). It may be these changes are more significant in the stalk than the cap of the fruiting body. It was not possible to measure some species as their stalks were physically too small to accommodate electrodes with 20 mm separation.

![Fig. 9](https://ars.els-cdn.com/content/image/1-s2.0-S1754504824000291-gr9.jpg)

Download: Download high-res image (600KB)

### 3.3. Exemplar recordings of S-parameters in mycelium-bound composites and fungal fruiting bodies over the 50 kHz to 3 GHz frequency range

Signal propagation in the mycelium-bound composite is frequency-dependent. shows S11 the return loss against frequency of exemplar recording. Resonance peaks are observed around 960 MHz, 1.05 GHz, 1.61 GHz, and 2.04 GHz.

![Fig. 10](https://ars.els-cdn.com/content/image/1-s2.0-S1754504824000291-gr10.jpg)

Download: Download high-res image (312KB)

Gain against frequency (S21) of exemplar recording of mycelium-bound composite is shown in. Resonance peaks in gain are observed around 64 MHz, 898 MHz, 1.17 GHz, 1.89 GHz, 1.99 GHz, and 2.70 GHz.

![Fig. 11](https://ars.els-cdn.com/content/image/1-s2.0-S1754504824000291-gr11.jpg)

Download: Download high-res image (346KB)

Return loss against frequency (S11) in cap and stalk of *[Agaricus bisporus](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/agaricus-bisporus "Learn more about Agaricus bisporus from ScienceDirect's AI-generated Topic Pages")* (Portobello) fruiting bodies, is shown in. Signal propagation was observed to be frequency-dependent with resonance peaks around 180 MHz, 780 MHz, 1.4 GHz, 2.1 GHz and 2.7 GHz.

![Fig. 12](https://ars.els-cdn.com/content/image/1-s2.0-S1754504824000291-gr12.jpg)

Download: Download high-res image (358KB)

Signal gain against frequency (S21) in cap and stalk of *Agaricus bisporus* (Portobello) fruiting bodies is shown in, with peaks in attenuation around 780 MHz, 1.18 GHz, 1.89 GHz, 2.07 GHz, 2.26 GHz, and 2.76 GHz.

![Fig. 13](https://ars.els-cdn.com/content/image/1-s2.0-S1754504824000291-gr13.jpg)

Download: Download high-res image (439KB)

Overall, [electrical characteristics](https://www.sciencedirect.com/topics/materials-science/electrical-property) were observed to vary with electrode separation. In other recordings not reported in this paper () a distance of ∼20 mm between centres of electrodes was found to be effective for measuring electrical properties. This suggests that there is an optimum spacing for the electrodes in any environment. Optimising the relative physical positions of electrodes in colonised substrate and fungal fruiting bodies is important to maximising the sensitivity of monitoring and interconnections to other systems.

## 4\. Discussion

A low-filter is described by its transfer function as shown below:(1) $H \left(\right. f \left.\right) = \frac{1}{\sqrt{1 + \left(\frac{f}{f c}\right)^{2}}} ,$where *f* is the frequency and *f* <sub><em>c</em></sub> the mean cut-off frequency. In [decibel](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/decibel), it is given in form of(2) $H \left(\right. f \left.\right)_{d B} = - 10 log \left(1 + \left(\frac{f}{f_{c}}\right)^{2}\right) d B$

When $\frac{f}{f_{c}} \ll 1$, *H* (*f*) <sub><em>dB</em></sub> ≈ − 10 log 1 = 0 meaning there is no attenuation of the input signal applied but starting from *f* <sub><em>c</em></sub> on-ward the signal suffers a significant attenuation. The growth of a strong hypha network through the body of well-colonised substrate and particularly near the [surface](https://www.sciencedirect.com/topics/immunology-and-microbiology/surface-property) of fresh spawn, with ∼80 % moisture content, appears to considerably raise the mean cut-off frequency to $>$ 500 kHz compared to ∼10 kHz with bare Rye seeds with ∼66 % moisture content and ∼50 kHz with Rye seeds moistened with mains water ∼76 % moisture content.

De-ionised water (2 ml with a conductivity of 10 MΩ cm) absorbed by open cell polyurethane foam sponge (electrical insulator, ∼50 ml volume) has the lowest mean cut-off frequency ∼5 kHz. It is reported that distilled water acts as a high-pass filter over 200 MHz to 9 GHz range (). Mains water (2 ml with a higher conductivity of 0.0025 MΩ cm) absorbed by open [cell foam](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/foam-cell) (∼50 ml volume) has a higher mean cut-off frequency ∼8 kHz.

Phase against frequency plots (b) roughly align with attenuation against frequency plots (a). The most noticeable inconsistency is water on insulating substrate above ∼50 kHz.

The physical mass of the spawn block (100 g vs 750 g) only has a modest affect on attenuation between electrodes with the same (20 mm) separation.

The lower mean cut-off frequency of fruiting bodies (5 kHz–50 kHz depending on species) may be applicable to a diverse range of applications; non-computing electronic circuits (e.g. signal filtering in audio systems (;; )), processing of sensory data at lower rates rather than ‘big data’ processing () (e.g. Edge Computing (;; )), analog computing (e.g. frequency filters in coupled oscillator computing (;; )).

Mycelium-bound composites with higher mean cut-off frequency (∼500 kHz) might be utilised in higher speed analog computing circuits (). For example, ‘switches’ based on controlled growth of hypha networks might form ultra-low power consumption signal routers (; ).

Living mycelium might be used for sensing, sensorial fusion, and pre-processing. Further, integrating mycelium and [silicon](https://www.sciencedirect.com/topics/materials-science/silicon) components (potential on dried mycelium ()) together might facilitate novel capabilities of analog computing hardware.

Low pass filter might be utilised to provide an upper bound on rate of data processing in any computational, logic gate circuitry either embedded in the substrates or made from the substrates.

In this work, we have characterised the samples using S-parameters which is a portable “black box” model that can be included in the simulation environments of several commercial tools. In S-parameter measurements S11 represents how much signal power is reflected from the sample. The accepted signal is either transferred, absorbed as losses within the sample, or radiated. *S* 21 represents the amount of energy transferred from port 1 to port 2.

For consistency, all measurements were conducted with same environmental conditions (temperature, humidity, illumination) with known species of fungi. However, as the properties of colonised substrate and fruiting bodies are affected by numerous parameters (including moisture content and growth of hyphae which are difficult to regulate) the results presented are exemplars rather ‘absolute’ values.

Obtaining fresh blocks of spawn (e.g. 100 g bags) from commercial suppliers at desired times was challenging (e.g. limited stock availability). Further, most commercial suppliers were unwilling to provide details of substrate composition (beyond “Rye seeds” as considered a ‘trade secret’). Therefore, variation in substrate might exist between both batches from the same supplier and different suppliers. The level of colonisation of blocks varied greatly between suppliers and times of recordings as the fungi consumed the substrate as a source of nutrients. Additionally, the heterogeneous mixture of substrate and fungi added an additional variable.

The scoping measurements presented in this study are limited and only point towards potential applications. However, a more detailed/extensive analysis (beyond the scope of this study) might reveal additional functionality that is useful for applications.

The ecological implications of our findings extend beyond the applications for mycelium-bound composites and fruiting bodies in analog computing and bio-hybrid systems (). The observed differences in cut-off frequencies between fruiting bodies and mycelial networks suggest to an underlying ecological strategy that fungi might employ in nutrient acquisition and inter-organism communication in their ecosystems (). This bio-communication has the potential to play an important role in ecosystem function, such as nutrient cycling, habitat structuring, and plant and [microbial community](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/microbial-community) regulation? Understanding these electrical properties opens up new opportunities for ecological research, offering a novel perspective on the interconnectedness of myceliated forest ecosystems ().

Furthermore, research into electrical properties in fungal networks could significantly enhance our methods for [monitoring ecosystem health](https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/ecosystem-monitoring). By integrating electrode arrays and electrically shielded cables in our measurement techniques, we can reduce noise and increase the resolution of our observations of fungal [electrical activity](https://www.sciencedirect.com/topics/immunology-and-microbiology/electric-activity) (). This advancement has the potential to improve the quality of our data while also enabling the development of non-invasive tools for real-time monitoring of ecosystem [dynamics](https://www.sciencedirect.com/topics/immunology-and-microbiology/dynamics). Custom-designed electrode arrays, for instance, enable spatially resolved measurements that can map the [physiological state](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/physiological-state) of mycelial networks over time, providing insights into forest ecosystem health and stress responses. Furthermore, we could apply this to [farming systems](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/farming-system) in which fungi play an important role, such as mushroom production or mycorrhizal-dependent crops ().

Signal pre-amplifiers could be installed at measurement sites to improve the signal-to-noise ratio further (beyond current recording methods) (). However, this is a technically complex and financially expensive approach as numerous high-performance pre-amplifiers are required to produce noise-tolerant signals with adequate amplification for subsequent processing. Machine learning and AI-based signal analysis provide additional possibilities (). This could be particularly useful for (near) real-time monitoring or communication in the future. However, such an AI-powered system would need extensive training to achieve the required level of performance ().

The ability to ‘signal back’ to the mycelium in artificial surroundings (such as a mushroom farm) or natural environments (such as an old-growth forest) might offer several benefits (both financial and environmental) (). However, further research is required to achieve desired outcomes.

## 5\. Conclusions

Mycelium-bound composites were electrically characterised for signal transfer analysis with the aim of using them in electronic applications such as bio-hybrid computing systems.

Mycelium-bound composites act as low-pass filters with a mean cut-off frequency of ∼500 kHz; with ∼−14 dB/decade roll-off, and mean attenuation across the pass band of $<$ 1 dB. Fruiting bodies have between one or two orders of magnitude lower mean cut-off frequency (5 kHz–50 kHz depending on species); with −20 dB/decade to −30 dB/decade roll-off, and mean attenuation across the pass band of $<$ 3 dB. The mechanism underlying frequency-dependent attenuation is uncertain. The fine networks of hyphae may be better able to carry high-frequency signals than ‘bulk’ volumes of water (such as a wet foam sponge).

Mycelium-bound composites and fungal fruiting bodies may be useful building elements in analog computing. For example, frequency filters in Oscillator Computing and sensory data handling in Edge Computing. Living mycelium might be used for sensing, sensorial fusion, and pre-processing. Furthermore, integration of mycelium networks and silicon components (potential on dried mycelium) might facilitate novel capabilities for the next generation of analog computing. It is evident from this study that mycelium-bound composites are very lossy low to high frequency range and demonstrates [dielectric properties](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/dielectric-property). Although they can be considered as [electrical insulators](https://www.sciencedirect.com/topics/materials-science/electrical-insulator), with the moisture content, the [electrical breakdown](https://www.sciencedirect.com/topics/materials-science/electrical-breakdown) voltage may be reduced, and therefore they are not suitable for high-voltage applications. Transferring electrical signals through mycelium is quite challenging, but mixing it with conductive particles would enable sustainable electronic designs in the future ().

Our research into the electrical properties of mycelium-bound composites and fruiting bodies not only paves the way for innovative bio-hybrid computing technologies, but also deepens our understanding of the ecological roles of fungi. By elucidating the electrical behavior of fungal tissues and structures, we contribute to a broader ecological narrative that recognizes fungi as integral components of ecosystem function and resilience. The implications of our work suggest that fungi, through their electrical properties, offer a unique lens through which we can explore the complex interactions that sustain forest and farm ecosystems. Future studies should aim to correlate electrical potential recordings with other environmental inputs such as soil pH, temperature, and moisture levels to further unravel the ecological significance of fungal electrical activity. Moreover, the potential for ‘speaking back’ to the mycelium, as suggested by, highlights the possibility of influencing fungal behaviours in ways that could benefit agricultural practices, such as optimising mushroom cultivation, mykorrhizal nurturing, and enhancing soil health and regeneration. Our findings underscore the need for interdisciplinary approaches that merge the fields of electronics, [mycology](https://www.sciencedirect.com/topics/immunology-and-microbiology/mycology), and ecology to fully harness the potential of fungal electronics in both technological, productive, and environmental contexts.

## Availability of data

The raw data required to reproduce these findings are available to download from [https://doi.org/10.5281/zenodo.7339710](https://doi.org/10.5281/zenodo.7339710). The processed data required to reproduce these findings are available to download from [https://doi.org/10.5281/zenodo.7339728](https://doi.org/10.5281/zenodo.7339728).

## CRediT authorship contribution statement

**Neil Phillips:** Writing – review & editing, Writing – original draft, Methodology, Investigation. **Roshan Weerasekera:** Writing – review & editing, Methodology, Formal analysis. **Nic Roberts:** Writing – review & editing. **Antoni Gandia:** Writing – review & editing. **Andrew Adamatzky:** Writing – review & editing, Resources, Funding acquisition, Conceptualization.

## Declaration of competing interest

The authors declare the following financial interests/personal relationships which may be considered as potential competing interests:Neil Phillips reports financial support was provided by European Commission. Nic Roberts reports financial support was provided by European Commission. Andrew Adamatzky reports financial support was provided by European Commission.

## Acknowledgements

This project has received funding from the European Union's Horizon 2020 research and innovation programme FET OPEN “Challenging current thinking” under grant agreement No 858132. We are grateful to Ann Miller's Speciality Mushrooms Ltd for information on their grain spawn. We thank Alejandro Ramirez at B&K Precision Corporation for guidance on 891 LCR meter.

## References

- ### Fungal biohybrid substrates for resilient sensing and embodied anomaly detection
	2026, Biosystems
- ### From the bench to the reactor: engineered filamentous fungi for biochemical and biomaterial production
	2025, Biotechnology for Biofuels and Bioproducts
- ### Electrical information flows across the sporocarps of two ectomycorrhizal fungi in the field
	2026, Scientific Reports
- ### Gradients of Aliveness and Engineering: A Taxonomy of Fungal Engineered Living Materials
	2026, Advanced Materials
- ### Review on mushroom mycelium-based products and their production process: from upstream to downstream
	2025, Bioresources and Bioprocessing
- ### Fungal Tissue as a Medium for Electrical Signal Transmission: A Baseline Assessment With Melanized Fungus Curvularia Lunata
	2025, IEEE Journal of Electromagnetics RF and Microwaves in Medicine and Biology