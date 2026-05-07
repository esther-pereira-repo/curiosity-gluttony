---
title: "Electrical signaling in fungi: past and present challenges"
source: "https://academic.oup.com/femsre/article/doi/10.1093/femsre/fuaf009/8090185"
author:
  - "[[Matteo Buffi]]"
  - "[[Julia M Kelliher]]"
  - "[[Aaron J Robinson]]"
  - "[[Diego Gonzalez]]"
  - "[[Guillaume Cailleau]]"
  - "[[Justine A Macalindong]]"
  - "[[Eleonora Frau]]"
  - "[[Silvia Schintke]]"
  - "[[Patrick S G Chain]]"
  - "[[Claire E Stanley]]"
  - "[[Markus Künzler]]"
  - "[[Saskia Bindschedler]]"
  - "[[Pilar Junier]]"
published: 2025-03-21
created: 2026-05-07
description: "Electrical signaling in filamentous fungi."
tags:
  - "clippings"
---
## Abstract

Electrical signaling is a fundamental mechanism for integrating environmental stimuli and coordinating responses in living organisms. While extensively studied in animals and plants, the role of electrical signaling in fungi remains a largely underexplored field. Early studies suggested that filamentous fungi generate action potential-like signals and electrical currents at hyphal tips, yet their function in intracellular communication remained unclear. Renewed interest in fungal electrical activity has fueled developments such as the hypothesis that mycorrhizal networks facilitate electrical communication between plants and the emerging field of fungal-based electronic materials. Given their continuous plasma membrane, specialized septal pores, and insulating cell wall structures, filamentous fungi possess architectural features that could support electrical signaling over long distances. However, studying electrical phenomena in fungal networks presents unique challenges due to the microscopic dimensions of hyphae, the structural complexity of highly modular mycelial networks, and the limitations of traditional electrophysiological methods. This review synthesizes current evidence for electrical signaling in filamentous fungi, evaluates methodological approaches, and highlights experimental challenges. By addressing these challenges and identifying best practices, we aim to advance research in this field and provide a foundation for future studies exploring the role of electrical signaling in fungal biology.

## Introduction

For all living organisms, sensing environmental stimuli and integrating this information to generate a response are fundamental processes for survival. There are several mechanisms that organisms use for this coordination, including electrical signaling. Electrical signaling constitutes a rapid and reliable way of intra- and intercellular communication (Katz 1961, Keener and Sneyd 2009).

Speculation about the importance of electricity in the functioning of a living organism dates back to 1780, following Luigi Galvani’s seminal observation of muscle contraction in response to electrical currents (Piccolino 1998). Since this discovery, the connection between electricity and biology has been extensively investigated (Piccolino 1998, Canales et al. 2018). The role of electricity in cellular communication has been primarily investigated in animals, in particular mammals, given its importance for the functioning of the nervous system. In animal models, the transmission of an electrical signal between cells is driven by action potentials that result from specific stimuli. Briefly, action potentials are defined as a response to changes in voltage across the cell membrane, which result from ion (e.g. Na <sup>+</sup>, Ca <sup>2+</sup>, or K <sup>+</sup>) redistribution across the membrane. Depolarization that causes the cell to reach a certain voltage threshold generates a “spike” that is characteristic of these action potentials, which can then propagate along a cell and pass between adjacent cells (Häusser 2000).

Electrical signaling is now recognized to be ubiquitous across all domains of life, from bacteria to animals and plants (Piccolino 1998, Brenner et al. 2006, Prindle et al. 2015). However, the mechanisms and outcomes of electrical signaling vary across these domains. For instance, processes mediated by electrical signaling for cell-to-cell communication include the excitation of muscles by nerves in animals (Piccolino 1998), the rapid closing of stomata or leaf traps in *Dionaea muscipula* (the Venus flytrap plant) (Böhm et al. 2016, Blatt 2024), and tissue regeneration and organization in plants (Nuccitelli 1988, 2003, Brenner et al. 2006, Clarke et al. 2013, Beagle and Lockless 2015, Prindle et al. 2015, Levin et al. 2017, Szechyńska-Hebda et al. 2017, McLaughlin and Levin 2018) and animals (Harris 2021). Unicellular organisms, such as bacteria found in biofilms, also utilize electrical signaling to aid in community coordination and response to environmental changes (Prindle et al. 2015).

In fungi, diverse electrophysiological behaviors, including the generation of action potential-like signals (Olsson and Hansson 1995) or the generation of currents in the hyphal tips (Stump et al. 1980, Gow 1984, Horwitz et al. 1984) were shown in studies conducted in the late 20th century. However, the role of electrical signaling as a mechanism of intracellular communication was not irrefutably shown in these early studies, and progress in the field stalled. Recent studies have sparked renewed interest in the topic, particularly in relation to the importance of filamentous fungi in soil ecosystems (Hunter 2023). The hypothesis of a “Wood Wide Web” considers plants being connected to each other via the common mycorrhizal network (CMN) (Simard and Durall 2011) and being able to communicate with each other using electrical signaling. This hypothesis is partly based on measurements of electrical currents in the plant–fungus interaction zone in roots, as well as the induction of changes in transmembrane potentials in germ tubes of mycorrhizal fungi exposed to plant root extracts (Berbara et al. 1995, Ayling et al. 2000). Although this highlights the potential importance of fungal electrical signaling at the level of ecosystems, the existence of the CMN and its role in interspecies communication is still highly debated (Karst et al. 2023). On the other hand, the proposed use of fungal mycelium for the generation of innovative materials with electric conductive properties such as sensors or so-called fungal computers (Li et al. 2022, Meyer 2022, Jo et al. 2023, Mayne et al. 2023, Hyde et al. 2024, Jones et al. 2024) has also contributed to the renewed interest in the area.

Fungi are a clade of eukaryotic microorganisms with remarkably diverse physiologies and metabolisms and can perform numerous ecological functions. Morphologically, fungi range from unicellular yeast to multicellular forms such as molds and mushrooms (James et al. 2020). Regardless of the apparent morphological complexity of one or the other growth mode, yeast and filamentous fungi are important models to study fundamental processes of eukaryotic cells (van der Klei and Veenhuis 2006). Moreover, filamentous fungi have been used by humankind as versatile and robust cell factories, but to exploit their full potential we need to overcome the limited knowledge of fungal biology (Meyer et al. 2016).

Multicellular filamentous fungi are tip growing organisms showing a radial three-dimensional growth of tube-like structures called hyphae. This morphology can be considered ideally suited for electrical signaling as hyphae contain a continuous plasma membrane and cell wall. Furthermore, the cell wall can be coated with hydrophobins (i.e. surface active amphiphile proteins) (Wösten and de Vocht 2000, Linder et al. 2005, Kulkarni et al. 2017) and other compounds such as melanin. These structural components and the cell wall polysaccharides could have a potential role in insulating the interior of the fungal cell, preventing electrical leaking, a function carried out by myelin in neurons (Morell and Quarles 1999). Filamentous fungi from basal clades (i.e. Mucoromycota) often have coenocytic (continuous cytoplasm) hyphae, but higher fungi (Dikarya) utilize septal pores to compartmentalize their hyphae continuum (Rayner et al. 1995, Fricker et al. 2007, Harris 2008). These pores regulate the exchange and transport of nutrients, macromolecules, organelles, and play a role in cellular differentiation and reproduction (Fischer 1999, Abadeh and Lew 2013). Septa can be closed by plugging to prevent loss of cytoplasm content after hyphal damage (Markham 1994, Steinberg et al. 2017), or in response to deleterious biological interactions such as mycoparasitism (Gimeno et al. 2021). This means that the cytoplasm in Dikarya is not always continuous and the propagation of chemical signals via cytoplasmic bulk flow can be inefficient. Conversely, plasma membrane continuity and, thus, electrical signaling, are not affected by septal pore plugging (Gow and Morris 1995, Roper and Seminara 2019). In this way, electrical signaling could still allow for communication between distant hyphae within a mycelial network, even during times of distress or physical disruption.

A fascinating feature of multicellular fungi is the formation of a mycelium, consisting of a network of interconnected hyphae that can grow, branch, fuse, and adapt dynamically to environmental conditions (Fricker et al. 2017). The formation of such networks allows filamentous fungi to improve nutrient acquisition and translocation (Rayner et al. 1995, Harris 2008, Fricker et al. 2017, Fischer and Glass 2019). The mycelial network is a highly dynamic structure and its plasticity in space and time allows fungi to cope with uneven or ephemeral distribution of resources in complex environments such as soils (Hutchings et al. 2000). The mycelium is inherently modular and provides an architecture that results in the adaptability needed to exploit resources and thrive in heterogeneous environments (Fig. 1). Each hyphal segment functions semiindependently, enabling the organism to allocate resources flexibly and respond locally to stimuli such as nutrient availability or stress. Experiments performed with wood rotting fungi have shown that network structure can change very rapidly when new resources are discovered by a foraging mycelial front (Wood et al. 2006). The speed and extent of the reorganization depend not only on the foraging strategy, but also on the size and quality of the new resource, and the presence of competitors (Wood et al. 2006). This observed capability to rapidly reorganize suggests the existence of one or several systems to integrate information from different areas in a mycelial network.

![Organization of a mycelial network. In soils, the mycelium needs to integrate a multitude of stimuli to coordinate the reorganization of its hyphal network. This allows to improve nutrient acquisition and exploration and colonization of complex habitats. This decentralized growth strategy underpins many unique features of fungal biology, including interactions with other organisms. Studying how mycelial networks integrate information across multiple spatial and temporal scales presents unique challenges, including the high spatial heterogeneity of actively growing structures such as hyphal tips, where electrical currents are known to be produced. Moreover, morphological elements such as septal pores, as well as the structure and composition of the cell, appear ideally suited for electrical signaling.](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/femsre/49/10.1093_femsre_fuaf009/1/m_fuaf009fig1.jpeg?Expires=1779996799&Signature=Ix635gyBsadqqfpF0Qul7DwoZQ-8xZ4I9Dh9sO9rzMZdqywwH3ODaKkYz82kOMUUvj-TU0mOTqVV44Kz2asgGMNAqUHV~7ySb0Gu9dfmuR~QbOO347nPMKZ7na7KLpjqSfsFiPczINn1chIeZp4lbDcs70sRiVOmHT3lh2pTjPQDbTUSt31BggUMTYuM0957-D1btIN3Vj9NvLY9uuV2e30iGNM2ISZmAE4EPkDkM2obBsqzaHyKu~QOXRU829XgYWHFZF0Y~lJMpuVHwAx7R8Yu2vQGb43URHHUpfhDjfrVg5sC1bGx7VLw72LSmCwtuxTTQjbUHoCV9C8JkamNRA__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)

Figure 1.

Organization of a mycelial network. In soils, the mycelium needs to integrate a multitude of stimuli to coordinate the reorganization of its hyphal network. This allows to improve nutrient acquisition and exploration and colonization of complex habitats. This decentralized growth strategy underpins many unique features of fungal biology, including interactions with other organisms. Studying how mycelial networks integrate information across multiple spatial and temporal scales presents unique challenges, including the high spatial heterogeneity of actively growing structures such as hyphal tips, where electrical currents are known to be produced. Moreover, morphological elements such as septal pores, as well as the structure and composition of the cell, appear ideally suited for electrical signaling.

[Open in new tab](https://academic.oup.com/view-large/figure/511922188/fuaf009fig1.jpg) [Download slide](https://academic.oup.com/DownloadFile/DownloadImage.aspx?image=https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/femsre/49/10.1093_femsre_fuaf009/1/fuaf009fig1.jpeg?Expires=1779996799&Signature=BCbMq6Y1hTraohlAc7AR7Pg4BFWJ81ny7w0VFVr6PMWIXSN6qHiB825hZnmxFfzOqMpbK5ZGz5YVkBmp0anfrdzwKqTXQI4y9nYajRtM54uSP4YEhvJu0IphTYth3FwPFkf8QFbtJUrxhxg-4kvO0ikWh7eZqe6quNlHrkfn-br-IepxQuhVad0wF7Vv9m~uMSyfVns~GMBYXgj-Jc~oHwdqwF2RxuuvHQIh36MmCd97psV6auMU63WO5ZrZQO5C5ibDIyQG8D4C5uZL66t1M48bGBrTfOXi3jIrRwfEPp~Wjts96JZynp27ApMQQ7FqAFJ6EwZjZd-~AKaSI79Kaw__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA&sec=511922188&ar=8090185&xsltPath=~/UI/app/XSLT&imagename=&siteId=5386)

Direct uptake and intrahyphal nutrient diffusion are considered sufficient to sustain short-range local growth when resources are abundant (Olsson 2001) or in slow-growing fungal species (Olsson and Jennings 1991a, b, Darrah et al. 2006, Ashford and Allaway 2007, Fricker et al. 2017). In other conditions, multiple transport pathways (Jennings 1987, Cairney 1992, Heaton et al. 2012) or pressure-driven delocalization of resources have been suggested as mechanisms behind nutrient redistribution (Lew 2011). The cost of these strategies is expected to increase the longer the distance (i.e. meters) to be covered in the mycelial network (Fricker et al. 2017). Passive movement with the mass flow resulting from the influx–efflux of water could provide a less costly alternative. However, this creates a risk of excessive evaporation given the high surface area resulting from an extensive mycelial network (Fricker et al. 2017). Moreover, passive movement cannot explain the inversed flux of nutrients observed in fungal structures such as fungal cords (Olsson and Gray 1998), which are specialized structures made of densely packed hyphae used for transport of nutrients and water over long distances (Townsend 1954). Inversed cytoplasmic movement has also been observed in other specialized hyphae such as trunk hyphae (Schmieder et al. 2019). Recent work mapped and observed bidirectional flow in almost all hyphae of *Rhizophagus irregularis* A5, *R. irregularis* C2, and *Rhizophagus aggregatum*. The fungal partners exchange nutrients with roots and thus bidirectional flow is essential to connecting the foraging point to the plant host. A higher flow speed in larger hyphae suggest the control of speed by the fungus to increase the volume exchanged in larger and more direct trunk hyphae (Oyarte Galvez et al. 2025). Pressure-driven delocalization is also difficult to reconcile with behaviors performed in distant areas of the mycelium (Roper and Seminara 2019). These examples suggest that filamentous fungi need a mechanism to control cytoplasmic flow, especially when the mycelium is extended and/or when it acts as an exchange channel between two points. A larger volume from a higher number of auxiliary hyphae connected to larger trunk hyphae could explain an increased flow. However, this requires a fine control of network organization, and there is no data available for the moment that supports this hypothesis. All of the above pledges in favor of a different process for long-distance network coordination as well as for coordinating the modular behavior of the mycelial network.

In other organisms such as animals, integration and response to environmental stimuli is coordinated by the nervous system, which uses electrical signaling for fast responses. However, the use of electrical signaling for communication and coordination of responses to environmental stimuli in plants shows that a central nervous system is not a requirement. In plants, electrical signaling regulates slower responses (e.g. response time in minutes to hours) primarily for adapting to environmental stresses and regulating physiological processes, but it is also used in faster processes such as the closing of the Venus’ fly trap or mimosa leaves. Electrical signaling in plants is mediated by the production of action potentials with the same key characteristics of those in animals, but with important differences in the molecular components of depolarization. While Na <sup>+</sup> ions are important in the generation of action potentials in animals, plants are thought to require Ca <sup>2+</sup> and Cl <sup>−</sup>, probably due to the high toxicity of sodium. Resting membrane potentials for plants are around −120 mV compared to the −70 mV for animals. Lastly, the speed of signal propagation in plants is typically slower than that in animals (for instance, 5–25 cm s <sup>−1</sup> in the Venus flytrap versus 0.1–100 m s <sup>−1</sup> in nerves) (Lee and Calvo 2023). In addition, electrical signaling in plants also includes the generation of variation and systemic potentials (Zimmermann et al. 2009, Vodeneev et al. 2015). Variation potentials are long-distance intercellular electrical signals to coordinate functional responses under stressors. Like in the case of action potentials, variation potentials are created by transient membrane depolarization, although the dynamics of membrane potential changes are different (Vodeneev et al. 2015). Similar to plants, fungi are sessile organisms that cannot escape stressors such as predators or nutrient scarcity, but must adapt locally. Accordingly, electrical signaling such as variation and systemic potentials could be some of the mechanisms behind the coordinated behavior of mycelial networks (Vodeneev et al. 2015).

The goal of this review is to provide an overview of the current evidence for the existence of electrical signaling in filamentous fungi and the challenges of applying traditional electrophysiological techniques for this specific type of microorganism. These challenges are not only due to the small dimensions of individual hyphae and the differentiation of cells (e.g. hyphal tip), but also to the spatial complexity of modular mycelial networks. In the second part of this review, we present a critical assessment of current methods and expose experimental caveats that we have encountered while trying to obtain novel evidence for electrical signaling in filamentous fungi. The objective of this second part is to help other research groups to avoid costly pitfalls and to encourage future studies in the area.

## Electrophysiological phenomena in fungi

In electrophysiology, one distinguishes two kinds of measurements, voltage and current. Voltage, or electrical potential, corresponds to a measure of the difference in charge between two points in an electrical field. In biological systems, this is often the membrane potential created by the differences in ion concentrations inside and outside of a cell (i.e. across membranes) (Kamada 1934, Curtis and Cole 1942). Monitoring changes in the membrane potential allows for the characterization of the process of depolarization and repolarization that occur during an action potential (Curtis and Cole 1942). In contrast, current is the flow of electrical charge per unit of time (per second). In biological systems, this can correspond to the movement of ions across membranes (e.g. through ion channels) or, in some cases, charge conduction along cells via electrons, ions, or specialized structures such as those observed in cable bacteria (Boschker et al. 2021). Overall, the studies published so far suggest that the currents transmitted along fungal hyphae are either of low intensity (µA cm <sup>−2</sup>) (Gow and Morris 1995) or low voltage (nV to µV), resulting in values lower than those that have been observed along animal neurons that are in the mV range (Olsson and Hansson 1995). Accordingly, a recording method needs to be not only adapted to the magnitude of currents to be measured, but it also requires spatial awareness as to where to perform the recordings given the potential complexity and diversity of mycelial networks. For instance, multiple studies have demonstrated that specific areas of the mycelium are active upon predator attack (Schmieder et al. 2019) or during the nutritional exchange with plant hosts in mycorrhizal fungi (Oyarte Galvez et al. 2025). The latter study also showed highly dynamic network remodeling. Accordingly, it can be supposed that electrical signaling will not occur equally in all areas of the mycelial network, nor that all hyphae or even hyphal segments are equally involved in the conduction of the signal. Thus, it is essential to understand and control where and what should be measured to avoid the creation or measurement of artifacts or to generalize the behavior from single point observations to the entire modular organism as in the case of filamentous fungi. In this section, we will first present studies focusing on measuring electrical potential in fungi, and then address the existence of ion channels in this microbial group. An overall summary of relevant studies related to measuring electrical signaling and their findings is presented chronologically in Table 1. However, in the next sections, the discussion of the results was organized accordingly to the approach used or the electrophysiological process investigated.

Table 1.

[Open in new tab](https://academic.oup.com/view-large/511922194)

Summary of relevant studies related to measuring electrical signaling and their findings is presented chronologically.

| Year | Author(s) | Fungus or fungi investigated | Other organisms | Method used | Studied structure | Key observations | Proposed function (when applicable) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1962 | Slayman and Slayman | *Neurospora crassa* |  | Microelectrodes | Hyphae | Membrane potential changes induced by potassium. Reduction of membrane potential in response to sodium azide or nystatin | Membrane potential could be at the basis of foraging and environmental sensing |
| 1974 | Jaffe and Nuccitelli |  | Fucoid embryo | Development of extracellular vibrating microelectrodes | Embryo | Measurements of current in a developping embryo | Methological milestone allowing for a less invasive extracellular method to measure currents |
| 1976 | Slayman et al. | *Neurospora crassa* |  | Glass microelectrodes | Hyphae | Detection of autonomous action potentials | Undefined function |
| 1976 | Neher and Sakmann |  | Frog muscle fibers | Development of the patchclamp method | Muscle cells | Study of single transmembrane channels in neuromuscle signal transmission | Methodological milestone allowing to study the role of transmembrane ion-gated channels in signal transmission |
| 1980 | Stump et al. | *Blastocladiella emersonii* |  | Extracellular vibrating microelectrodes | Mycelium | Current patterns appear to play a role in the spatial localization of fungal growth and development | Possible function in growth and development |
| 1983 | Barbara, Armbruster and Weisenseel |  | *Achlya debaryana* (Oomycete)\* | Extracellular vibrating microelectrodes | Hyphae and sporangia | Relationship between currents and the formation of asexual sporangia | Involvement of currents in development |
| 1984 | Kropf et al. |  | *Achlya bisexualis* (Oomycete)\* | Extracellular vibrating microelectrodes | Hyphae | Transcellular electric currents associated to a proton/amino acid symporter | Amino acid (nutrient) absorbtion and hyphal polarization during growth |
| 1984 | Gow | *Neurospora crassa, Aspergillus nidulans, Schizophyllum commune, Mucor mucedo*, and *Coprinopsis cinerea* |  | Extracellular vibrating microelectrodes | Hyphae | All growing hyphae tested produced currents, but not hyphae that were not growing. The signal was proportional to the size of hyphae | Involvement of electrical current in growth of different fungi |
| 1984 | Horwitz et al. | *Trichoderma harzianum* |  | Extracellular vibrating microelectrodes | Hyphae | Light stimulated formation of conidia. Inward currents at the tip and outer currents along hyphae. | Early biophysical reaction to light |
| 1984 | Potapova et al. | *Neurospora crassa* |  | Microelectrodes | Hyphae | Membrane potential responds to blue light illumination | Response to blue light |
| 1986 | Kropf |  | *Achlya bisexualis* (Oomycete)\* | Microelectrodes | Hyphae | Depolarization caused by respiratory inhibitors | Intra cellular communication in response to stressors |
| 1986 | McGillivray and Gow | *Neurospora crassa, Aspergillus nidulans, Mucor mucedo*, and *Trichoderma harzianum* | *Achlya bisexualis* (Oomycete)\* | Electrophoresis machine | Mycelium | Electrical fields affect the polarity of growth including germ tube formation and branching, the direction of hyphal extension and the frequency of branching and germination | Polarity of hyphal growth may be under electrical control |
| 1988 | Youatt et al | *Allomyces macrogynus* |  | Extracellular vibrating microelectrodes | Rhizoids and hyphae | Outward flow of positive electrical current behind the apex and inward flow around rhizoids | Localized nutrient transport linking symport of nutrients (e.g. amino acids or phosphate) with protons |
| 1989 | Gow | *Allomyces macrogynus* and *Basidiobolus ranarum* | *Achlya bisexualis* (Oomycete)\* | Extracellular vibrating microelectrodes | Rhizoids and hyphae | Electrical currents are driving the expansion of the hyphal apex or maintaining cell polarity | Inward electrical current reflects local nutrient transport and not local cell growth |
| 1992 | Garril et al. |  | *Saprolegnia ferax* (Oomycete)\* | Patch clamp | Protoplasts in different areas of the hyphae and hyphal tips | Presence of large Stretch-activated Ca <sup>2+</sup> and K <sup>+</sup> permeable channels and a small Mg <sup>2+</sup> in the hyphal tip, and the first two along the hyphae | Participation of Strech-activated channels in tip growth and Ca <sup>2+</sup> -activated K <sup>+</sup> channels in turgor pressure |
| 1993 | Garril et al. |  | *Saprolegnia ferax* (Oomycete)\* | Patch clamp | Protoplasts in different areas of the hyphae and hyphal tips | Inhibitory effect of gadolinium on growth and on Stretch-activated Ca <sup>2+</sup> channels at the tips. Inhibtion of Ca <sup>2+</sup> -activated K <sup>+</sup> channels along hyphae by tetraethylammonium, causing a rapid but transient decrease in growth | Stretch-activated Ca <sup>2+</sup> permeable channels as sensors for hyphal tip mechanical stress. Entry of Ca <sup>2+</sup> at the tip is foundamental for growth |
| 1994 | Garrill and Davies |  | *Saprolegnia ferax* (Oomycete)\* | Patch clamp | Protoplasts in different areas of the hyphae and hyphal tips | Direct measurement of ion channels on the membrane | Cell signaling, cell polarity, pH regulation, growth and differentiation, reproduction, nutrient uptake, turgor regulation, and pathology |
| 1995 | Olsson and Hansson | *Armillaria bulbosa* and *Pleourotus ostreatus* |  | Glass microelectrodes | Cords and “loose” tissue | Recording action potential-like signals in response to external stimuli | Sensing and communication in distant areas of the mycelium |
| 1995 | Berbara et al. | *Gigaspora margarita* | *Trifolium repens* and *Daucus carota* | One dimensional vibrating probe | Hyphae | Electrophysiological dimension to the plant fungus interaction and modulation of ion transport in the early events iof a mycorrhizal symbiosis | Modulating mycorrhizal interaction with roots and spore germination |
| 1997 | Roberts et al | *Aspergillus niger* |  | Patch clamp | Ablated hyphae | Description of an anion-selective efflux channel in the plasma membrane | Role of Cl <sup>−</sup> efflux on tip growth and pH homeostasis |
| 2018 | Adamatzky | *Pleurotus djamor* |  | Subdermal needle electrodes | Fruiting bodies | Recording of trains of spikes (action potential-like signals) in fruit bodies that was correlated with translocation of nutrients and relocation of products of metabolism | Use of action potentials in physiology and communication |
| 2021 | Adamatzky and Gandia | *Ganoderma resinaceum* |  | Subdermal needle electrodes | Fruiting bodies | Similarities between trains of spikes in another mushroom-forming species | Action potential-like spikes may correspond to fungal language |
| 2022 | Adamatzky | *Omphalotus nidiformis, Flammulina velutipes, Schizophyllum commune*, and *Cordyceps militaris* |  | Subdermal needle electrodes | Fruiting bodies | Species-specific spikes patterns | Action-potential-like spikes resemble human speech |
| 2022 | Thomas and Cooper | *Glomus intraradices, Glomus aggregatum, Glomus mosseae*, and *Glomus etunicatum* | *Pisum sativum* and *Cucumis sativus* | Glass microelectrodes (in the plant stems) | Interface plant–fungi | Transfer of electrical signals from one plant to the other | Interspecies communication |
| 2024 | Fukasawa et al. | *Pholiota brunnescens* |  | Six subdermal electrodes around a Petri dish | Mycelium | Electrical signal transfer and whole-body integration in fungal mycelia | Participation of electrical currents in fungal behavior |
| 2024 | Jones et al. | *Curvularia lunata* |  | Copper electrodes | Mycelium | Tissues from the fungus could potentially serve as a component in low-frequency biosensors for signal transmission | Mycelium as a biosensor |
| 2024 | Pajić et al. | *Phycomyces blakesleeanus* |  | Nano surgical ablation of cell wall + patch clamp | Hyphae | New faster and less invasive laser for laser ablation of the cell wall | Methodological milestone allowing future studies on the role of transmembrane ion-gated channels in signal transmission |

\*

Oomycetes were classified at the time as fungi.

#### Electrical measurements in microscopic fungal structures

The study of electrical signaling in microscopic fungal structures has been difficult due to technical challenges, particularly in recording internal currents in hyphae. Two of the most traditional methods to record action potentials are the voltage or current clamp. The patch clamp method, introduced by Neher and Sakmann in 1974 (Neher and Sakmann 1976) using frog muscle fibers, enabled the direct measurement of ion channel activity. This method involves forming a high-resistance seal between a glass pipette and a small patch of the cell membrane, allowing for the measurement of membrane potential and ionic currents with high precision (Neher and Sakmann 1992). Traditional patch-clamp techniques are reliable and widely applied in biological systems (Hamill et al. 1981, Zhao et al. 2008), but face limitations in fungal hyphae mainly due to their size (2–10 µm), but also to the presence of a cell wall and its associated proteins (Martinac et al. 2008). Accordingly, measurements with this approach have been mainly conducted in protoplasts obtained through enzymatic digestion on fungi-like cells of the oomycete *Saprolegnia ferax* (Garrill et al. 1992, 1993, Garrill and Davies 1994), or by laser ablation of the cell wall in *Aspergillus niger* (Roberts et al. 1997). Very recently, a novel method was utilized for nano-surgical ablation of the cell wall across multiple locations, which provides a new approach for protoplast generation in living hyphae that can be amenable to future patch-clamp studies of ion channels and their properties in filamentous fungi (Pajić et al. 2024).

In spite of all the challenges, electrophysiological behaviors have been studied since the late 20th century in several fungal species (Gow 1984, Harold et al. 1985, Gow and Morris 1995). The first studies were based on the use of intracellular glass microelectrodes. For this, sharp electrodes are used to penetrate the cell membrane, allowing researchers to record voltage (differential between two points in the colony or between the inside and outside of the cell membrane). This type of approach has been particularly useful for measuring the resting membrane potential and action potentials in neurons, providing insights into cellular excitability (Brette and Destexhe ). The method can be applied to several types of microorganisms, and the first intracellular electrical recording ever made was the measurement of the resting membrane potential in *Paramecium* (Takeo Kamada 1934). The first example of their use in fungi was the detection of electrical currents in the apex of growing hyphae in *Neurospora crassa*. Differences in membrane potential between the colony border (i.e. apex region) and the area toward the center of the colony were linked to polarized growth (Slayman and Slayman 1962). Glass microelectrodes inserted with micromanipulators to penetrate the fungal cell wall were also used for recording spontaneous voltage fluctuations resembling action potentials in fungi (Slayman et al. 1976, Olsson and Hansson 1995). Conventional glass microelectrodes were directly inserted into the hyphae of *N. crassa*. The spontaneous action potential-like behavior in this species involved depolarization and repolarization of the membrane with an apparent refractory period, similar to action potentials (Slayman et al. 1976). In another study with cords of *Armillaria bulbosa*, similar action potential-like signals were induced when the growing mycelium contacted a piece of beech wood that was initially placed 1–2 cm away from the colony (Olsson and Hansson 1995). The signals recorded in cords were measured using a glass microelectrode that was inserted among the mycelial strands, with a reference electrode inserted into the agar medium. *Pleurotus ostreatus* was tested with the same approach, and similar results (i.e. recording of action potential-like signals) were obtained in so-called “looser” tissue located at the edges of the colony. In both cases, the rate of spontaneous firing was very similar (frequency of 0.5–5 Hz and amplitude of 5–50 mV) to that recorded in animal sensory systems. However, this invasive approach could have altered fungal behavior, potentially compromising the validity of the data. In addition, as shown by this pioneering work, this approach cannot be generalized to all cell types of filamentous fungi, as the recordings were unsuccessful with undifferentiated hyphae (Olsson and Hansson 1995).

Further studies were possible thanks to the development of extracellular vibrating electrodes that allow the extracellular recording of hyphae-generated currents (Jaffe and Nuccitelli 1974, Nuccitelli 1990). Vibrating microelectrodes are used primarily to measure extracellular ion flow and electric fields. This technique involves the vibration of a microelectrode at a fixed frequency, which helps to detect small changes in voltage related to ionic movement in tissues. This approach is particularly useful in studying bioelectric fields generated by excitable tissues such as the heart and nervous system in a less invasive manner (Dorn and Weisenseel 1982, Nuccitelli 1990). Vibrating microelectrodes have been employed in various studies to measure currents around growing hyphal tips, during sporulation, and in response to light stimuli (Stump et al. 1980, Gow 1984, Horwitz et al. 1984). The first studies in fungi were inspired by the measurements of a positive current entering the rhizoid and leaving by the thallus in the aquatic fungus *Blastocladiella emersonii*, in which the current was believed to be carried by protons (Stump et al. 1980). Similar studies with the oomycete *Achyla* showed that currents were driven by a proton flow (inwards in the tip and outwards in the region away from it and toward the center of the colony) (Armbruster and Weisenseel 1983, Kropf et al. 1984). In *Achlya*, the use of intracellular microelectrodes afterwards helped to demonstrate that respiratory inhibitors produce the rapid depolarization of the membrane, indicating that membrane potential is governed by an electrogenic ion pump (Kropf 1986). The initial work with vibrating microelectrodes in *B. emersonii* and *Achlya* was later replicated with filamentous fungi including *N. crassa, Aspergillus nidulans, Schizophyllum commune, Mucor mucedo*, and *Coprinopsis cinerea*, all of which generated electrical currents (varying between 0.05 and 0.60 µA cm <sup>−2</sup>) around their hyphal tips (Gow 1984). Furthermore, the formation of light-stimulated conidia in *Trichoderma harzianum* was also proposed to be the result of electrical currents of different intensities applied along the hyphae. The modification of the currents in the membrane (outwards current in the sites stimulated by the light) was recorded 1–2 h after photoinduction (Horwitz et al. 1984). Similar experiments performed with microelectrodes and using blue light as stimulus suggested light-induced responses in *N. crassa*. The response in this case may not occur in every cell but the signal can be transmitted to the adjacent cells by means of electrical or chemical communication (Potapova et al. 1984).

The generation of inward electrical currents in the apex was initially linked to the regulation of the direction of growth of hyphae. The proposed model suggested that currents in the apex helped the directional growth of hyphae by providing a mechanism (i.e. establishing intracellular electrophoretic fields) explaining the movement of vesicles from the hyphal tip to the apex (Gow 1984). Accordingly, a study applying an external electric field showed that sites of germ tube formation and branching, the direction of hyphal extension, and the frequency of branching and germination can be affected by electric fields in some filamentous fungi including *N. crassa, A. nidulans, M. mucedo*, and *T. harzianum* (McGillivray and Gow 1986). However, another study measuring electrical currents with vibrating electrodes using the aquatic fungus *Allomyces macrogynus*, which produces true hyphae and rhizoids, presupposed a different behavior given its unique mechanism of cell wall deposition. Consequently, measurements with extracellular vibrating electrodes showed outward positive electrical currents around hyphae regardless of their growth status (extending or nonextending). In contrast, inward currents were detected in the rhizoids. The authors also did not find evidence indicating the role of calcium, while sites of nutrient uptake were correlated with inward electrical currents (Youatt et al. 1988). A follow-up study including *A. macrogynus* together with the soil fungus *Basidiobolus ranarum*, and the oomycete *Achyla bisexualis*, showed that inward electrical currents reflect local nutrient transport and not local cell growth, by linking together proton and nutrient symport (Gow 1989). Overall, these studies suggest that the role of electric currents on the hyphal tips in the redirection of growth cannot be generalized (Potapova 2012).

The use of vibrating microelectrodes is not without drawbacks. They are difficult to build and to operate correctly. Furthermore, the vibrating nature of the electrode can disturb biological processes (Jaffe and Nuccitelli 1974). Moreover, as the recordings are done extracellularly, they are often susceptible to background noise interference, thus requiring the inclusion of carefully designed controls and the use of systems such as a Faraday cage, which has been included in some but not all studies published so far. Recording signals in single hyphae does not only pose a problem due to the small size of individual hyphae relative to the electrode (usually on the order of 5 µm), but also by the complex organization of the fungal mycelium. When grown on a solid substrate such as an agar-based medium, it is virtually impossible to study individual hyphae, which can differ in their signaling activity, due to factors such as age or conditions of the local environment. This has been clearly shown, for instance, in experiments investigating the coordination of the response of *C. cinerea* to attacks by fungivorous nematodes. In this case, only specialized hyphae (called trunk hyphae) were shown to propagate chemical defense signals, while no activity was observed for a large fraction of the rest of the mycelial network (Schmieder et al. 2019).

The initial discovery of endogenous electrical fields at the hyphal tips prompted follow-up studies evaluating the effect of external electrical fields on the polarity of fungal growth as mentioned previously (McGillivray and Gow 1986). Fungi have shown both galvanotropic behavior, i.e. change of the direction of growth in response to an electrical field (Lever et al. 1994, Brand and Gow 2009) and electrotactic behaviors, i.e. active movement of a motile cell (e.g. zoospores) in response to an electrical field (Morris and Gow 1993, Swafford and Oakley 2018). The model organism *Candida albicans* has been fundamental to understanding the mechanism by which electrical fields affect the direction of growth. Germination experiments have shown that electrical fields modify the position of germ tubes likely by inducing the influx of Ca <sup>2+</sup> via the voltage-gated channel Cch1. This is supported by deletion of Cch1 or in medium containing a pharmacological Ca <sup>2+</sup> -channel blocker (i.e. BAPTA), which resulted in a severe attenuation of galvanotropism. Reciprocally, the response was enhanced in media with high extracellular Ca <sup>2+</sup> concentration (Brand et al. 2007). The galvanotropic response of hyphae of *A. nidulans, N. crassa*, and *C. cinerea* was pH- and Ca <sup>2+</sup> -dependent, suggesting also the implication of voltage-gated channels (Lever et al. 1994), as in the case of *C. albicans*.

Electrotaxis of zoospores of fungi-like oomycetes such as *Pythium* was triggered by electric fields of the same magnitude as those measured in plant roots (Morris and Gow 1993). Likewise, electrotaxis could be among the sensory mechanisms directing the movement of motile zoospores in zoosporic fungi. Wounding is known to generate an endogenous electric field in both plants and animals. In animals, this endogenous electric field serves to guide the movement of epithelial cells and other cells involved in wound healing to the wound site. In plants, these currents can lead to local hydraulic pressure and to a systemic potential trough the phloem to activate defenses (Tyler 2017). In accordance with the existence of this endogenous electric fields in their potential hosts, electrotaxis could participate in the localization of a suitable site for plant infection such as wounded areas. Zoosporic fungi are typically characterized as saprobes or parasites of both plant and animal hosts. Their zoospores have a finite amount of endogenous energy reserves and must locate quickly a suitable substrate or host. During dispersal of the zoosporic life stage, interpretation of environmental cues is critical for the survival and success of the future colony, and enhanced germination has been shown in weak electric fields (Moratto et al. 2023). Recently, an experimental system has been developed using zoospores of the saprotroph *Allomyces arbusculus*. This system demonstrated the combined role of photo and chemotaxis as part of a multisensory system acting during dispersal and settlement of zoospores (Swafford and Oakley 2018). This model could be used in future studies to evaluate the role of characteristic endogenous electric fields of a root or epidermis wounds (Jia et al. 2021) in guiding zoospore movement. The mechanisms explaining electrotaxis have not been elucidated in detail, but as in the case of galvanotropism, earlier studies suggest that this electro-guided movement is associated with Ca <sup>2+</sup> transport across the membrane (Morris and Gow 1993).

Moreover, fungi have been found to display thigmotropism (Jaffe et al. 2002, Stephenson et al. 2014), which is a directional growth movement in response to a touch stimulus. Thigmotropism is modulated by electric signaling in other organisms such as plants and animals (Sibaoka 1966, Jaffe et al. 2002). In *C. albicans*, thigmotropism, like galvanotropism, is attenuated by decreased Ca <sup>2+</sup> availability. Deletion of *CCH1* or the genes encoding two other transmembrane Ca <sup>2+</sup> channels (i.e. Fig. 1 or Mid1—a mechanosensor channel that activates calcium influx via Cch1), reduces the sensitivity of hyphal tips to topographical features in the substratum. These observations suggest that a localized Ca <sup>2+</sup> signal modulated by specific plasma-membrane Ca <sup>2+</sup> channels relay topologic information to direct tip growth (Brand et al. 2007, Kumamoto 2008, Brand and Gow 2009). In other fungi, the mechanism is still unclear but a change in membrane potential can be observed at the tip of the *N. crassa* during thigmotropic responses (Stephenson et al. 2014).

#### Electrical currents at the interface with other organisms

Measurements of electrical currents at the interface between roots of *Trifolium repens* (L. cv. New Zealand White), *Daucus carota* (L. cv. Nantes), and the mycorrhizal fungus *Gigaspora margarita* (Berbara et al. 1995) suggested a potential role of electrical signaling in interspecies communication. This mechanism of communication could provide a basis for plant-to-plant interactions via the connecting mycelium (Gilbert and Johnson 2017). Electrical signals may be produced by plants in response to mechanical damage (Mousavi et al. 2013, Johnson and Gilbert 2015) and be propagated by the mycelium, making the fungal network act as a “communication cable” between plants (Johnson and Gilbert 2015). A more recent paper attempted to demonstrate this experimentally using mycorrhizae (Thomas and Cooper 2022). For this, two plants (*Pisum sativum* and *Cucumis sativus*) were linked via a mycorrhizal network creating a bridge that connected two separate agar plugs. The plugs were inoculated with a commercial inoculum containing several species of the *Glomus* genus (*Glomus intraradices, Glomus aggregatum, Glomus mosseae*, and *Glomus etunicatum*). The electrical recording was made by inserting glass microelectrodes into the stems of the plants. The authors concluded that electrical signals were reliably conducted across the mycelial bridges from one plant to the other upon the induction of a wound response (Thomas and Cooper 2022). The method and the interpretation of the data has generated criticism, mostly on the lack of evidence of the biological origin of the voltage changes measured and on the need for a better mechanistic understanding of the processes that would give rise to these currents (Blatt et al. 2023). Also, it is not possible to rule out the conversion of an electrical signal into a chemical signal in the connecting mycelium. In addition, the use of an agar-based system can result in the generation of so-called Donnan potentials. A Donnan potential refers to the electrical potential difference that arises across a semipermeable membrane when charged particles are distributed asymmetrically due to the presence of impermeable ions (Petsev 2004). This occurs typically when using agar, which acts as a semipermeable membrane in combination with an ionic solution (e.g. culture media). The gel-like nature of agar enhances this effect, allowing the development of electrochemical gradients that produce Donnan potentials. Moreover, another aspect that was problematic in the experimental design is the recording of an electrical current when the mycelium was replaced by a thread, hinting to a physical phenomenon rather than to a biological one (Blatt et al. 2023). Nonetheless, despite the criticisms on these experiments, electrical communication is still postulated as one of the mechanisms for interspecies communication in soils (Hunter 2023).

Another area in which interspecies interactions could be mediated by electrical signaling is plant–pathogen interactions. Experiments performed with motile zoospores of the fungus-like Oomycete *Phytophthora palmivora* and *Arabidopsis thaliana* and *Medicago truncatula* showed that the external application of a weak electric field can alter the attachment of the zoospores to the roots. These findings and understanding the underlying mechanisms can be important to provide future paths to co-opt those mechanisms to protect crops (Moratto and Sena 2023, Moratto et al. 2024). Similar mechanisms could affect the interaction of both beneficial and pathogenic fungi with plant roots.

#### Electrical measurements with macroscopic structures

Since 2018, several studies have investigated the production of action potential-like electrical currents in mushrooms. These studies were inspired by work performed on slime molds with the overall goal of developing sensing and computing systems based on filamentous fungi (Adamatzky 2018b). In the first of these studies, electrical potentials were recorded in fruiting bodies of *Pleurotus djamor*. Electrical activity was measured with subdermal needle electrodes that were inserted into the stalk and the translocation zone of the cap. Electrical activity (voltage potential) was recorded with a high-resolution data logger (ADC24, Pico Technology) with technical features that were touted to reduce noise (twisted cables for electrodes). The measurements made suggested that fruiting bodies exhibit spontaneous “spiking” behavior. This spontaneous behavior corresponded to a slow drift from a base voltage potential, combined with relatively fast (starting 3 s after stimulation) oscillations of the potential. In addition, the impact of chemical and thermal stimulation was investigated. Negative or positive spikes (i.e. depolarization and hyperpolarization) were detected upon stimulation (Adamatzky 2018a). In a follow-up study, the same approach was used to measure electrical activity in *Ganoderma resinaceum* (Adamatzky and Gandia 2021). Further tests using four fungal species (*Omphalotus nidiformis, Flammulina velutipes, S. commune*, and *Cordyceps militaris*) resulted in differences in the patterns obtained. This prompted the authors to propose that those differences convey species-specific information and the existence of a language derived from electrical activity (Adamatzky 2022). Although the methodology applied appeared to be promising for the advancement of the field, some aspects of the experimental design and the interpretation of the results have been criticized by some authors (Blatt et al. 2024). A considerable element of criticism is the fact that part of the electrical activity likely originates from voltage fluctuations that do not have a biological origin. For instance, the use of stainless-steel needles is prone to the recording of Donnan potentials (Blatt et al. 2024). A similar approach has been used recently to measure electrical responses in the basidiomycete *Pholiota brunnescens* during growth in agar plates over a long period of time (100 days). Electrical potentials were measured extracellularly with electrodes inserted in the plates and the results were analyzed based on the colonization of areas of electrodes. The authors claimed to have recorded the longest electric oscillation on this system (1 week oscillation cycle) (Fukasawa et al. 2024). Considering the methodology used (agar-based cultivation and extracellular electrodes), this study presents potentially similar experimental flaws as other studies in which abiotic fluctuations cannot be ruled out (Blatt et al. 2023). A different kind of study in which a fungal mycelial mat of the ascomycete *Curvularia lunata* was placed between two electrodes suggested that fungal biomass can serve as a low-speed data transmission medium (Jones et al. 2024). All these studies attest as to the potential for the generation of novel materials with electric conductive properties using mycelium.

Given the promising results and ease of design proposed to study mushrooms with needle electrodes (Adamatzky 2022), we attempted to replicate this experimental system and assessed some of the caveats indicated by other authors (Blatt et al. 2024). To do so, we used a related mushroom-producing Basidiomycete, *Pleurotus pulmonarius*, because of its fast growth and ease of fructification. The goal of these experiments was the independent replication of the method. Accordingly, we used the same recording device (ADC-20 with a ADC20/24 Terminal Board; Pico Technology Ltd) and subdermal needle electrodes with twisted cables (Neurodart, spes Medica) (Fig. 2A–D). Additional information on the growth conditions of the fungus is presented in the [Supplementary information](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/femsre/49/10.1093_femsre_fuaf009/1/fuaf009_supplemental_file.docx?Expires=1779996799&Signature=oYVQv9pTp8zFkRcukBto6zQDeB1JPnG5NDk~bJssGVUCqQIrxP7aU4JG2Nhory9xmiIFQwzeC3IcyzDFMaUDXF229LuPVfj~zBWvpbZvSvvJGFUAn8MeFH--ImkD9FUNVMkWc9ed5DbuC8cClhsRvVFeX36qZ6d0m0Uajmx408OR6OIguAYnSTljrAbwH7I0oMbsAQavUlxsWaWmiQw9dSco~bKJmB06mRT28YxNWz4TLdKw~gUV9Sx5aFmgua3kpRHs~D1tG6-qjPosWmLMe5fJ01Qpvw1TWAee3P9f~qjLi3AjmGgWm1A82FSVeyAqAjFL~IVN~tdmj~Y8-9atRg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA). We inserted the needles into newly formed fructifications (Fig. 2E) and, as a control, we placed one of the differential electrode pairs into uncolonized substrate (Fig. 2F). Additionally, we cut one of the fructifications (Fig. 2G) and observed the evolution of the voltage potential recording (Fig. 2H and I). In the fruiting bodies, multiple positive and negative spikes were observed (blue, pink, and gray lines; ranging from above 50 to up to −300 mV). After detaching one of the fructifications (gray line), the signal resembled those recorded in the uncolonized substrate (dark violet), which corresponded to a cyclic signal with an amplitude of around 0.005 Hz (Fig. 2I). This suggested that the spikes were produced only while the fruiting body was attached to the fungus. This experiment confirmed the reproducibility of the recording method for fruiting bodies (Adamatzky 2022). However, we also observed signal changes due to the opening of the incubator door, the presence of people walking near the incubator or even the automatic closing of window shades behind the incubator in both the fungus and the control (i.e. positive and negative spike recorded at 18 and 42 h). This agrees with some of the criticisms of the method, in particular regarding the potential for recording of noise. Thus, a more controlled setting, such as a Faraday cage, is essential to improving this approach.

![Measurement of voltage fluctuations with needle electrodes inserted in fruiting bodies of the agaricomycete P. pulmonarius: (A) Scheme illustrating the insertion of the needle electrode into the foot of the P. pulmonarius fructification. (B) Images of the open incubator (POL-EKO-APARATURA sp.j, type: st 3C SMART) in which the experiments were performed; an aquarium lamp (Dennerle nanolight, 11 W) was located at the top. A humidifier (Stylies Alaze SC21011) and a recipient with moist vermiculite were placed at the bottom to maintain humidity. (C) ADC20/24 Terminal Board (Pico Technology Ltd) used to connect the cables to the datalogger. (D) Image of the data logger ADC-20 (Pico Technology Ltd) with four pairs of differential neurological subdermal needles with twisted cables (Neurodart, spes Medica). Needles were inserted through polystyrene pieces to ensure that the needles were located at a fixed distance (1 cm from one another). (E) Needle electrodes attached to three different fructifications of one fructifying bag of P. pulmonarius. (F) One pair of needle electrodes was inserted in the substrate without fungus as a control. (G) Fructification with inserted electrodes cut from the fructifying bag (1 day after insertion of the electrodes). (H) Raw signal recorded on the Picolog 6 software (Pico Technology Ldt). The red box represents the zoomed area shown in (I), in which we observed the effect of cutting off the fructification shown in (G). (I) Magnification of the red box from (H). Comparison of a signal for a fructification before and after cutting. Lines in blue, pink, and gray correspond to three different fructifications, while the uncolonized control corresponds to a dark violet line visible after the cut of the fruiting body in (G). After the cut, it is possible to observe the signal from the cut fruiting body (gray) resembling that of substrate control (dark violet).](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/femsre/49/10.1093_femsre_fuaf009/1/m_fuaf009fig2.jpeg?Expires=1779996799&Signature=I0yWeUv91xHfqW4vobPBvXafVOiW38qD1NXbLi32rpx9siRGMDetPA~dtOA3paXP7f~0ue1bBbYB6MyGPxhDaqsJxm6WUczU6ZIBmrLUCT-fexl5G~kQuWKKul3p26zFimR56fxQwWC-MeBlVh1IbWDK~yxFnwZf6ouAujl4Du0xGfCxLyfmveBEc4z9CIn0cwzMgI0RzRDh3-vtjluSxK6KWIrBtNIPDYaz7BuS4gNwmlX6R0sl4nAiGm7DBxhJLV3vddcETQYHwvmZ6Zrjei~~Ytyh~sX~0bHglMlLdgI8R46v2z~CCIJpjJUWrMjgrBEwZYWB7S4l2ivH9tYIxQ__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)

Figure 2.

Measurement of voltage fluctuations with needle electrodes inserted in fruiting bodies of the agaricomycete *P. pulmonarius*: (A) Scheme illustrating the insertion of the needle electrode into the foot of the *P. pulmonarius* fructification. (B) Images of the open incubator (POL-EKO-APARATURA sp.j, type: st 3C SMART) in which the experiments were performed; an aquarium lamp (Dennerle nanolight, 11 W) was located at the top. A humidifier (Stylies Alaze SC21011) and a recipient with moist vermiculite were placed at the bottom to maintain humidity. (C) ADC20/24 Terminal Board (Pico Technology Ltd) used to connect the cables to the datalogger. (D) Image of the data logger ADC-20 (Pico Technology Ltd) with four pairs of differential neurological subdermal needles with twisted cables (Neurodart, spes Medica). Needles were inserted through polystyrene pieces to ensure that the needles were located at a fixed distance (1 cm from one another). (E) Needle electrodes attached to three different fructifications of one fructifying bag of *P. pulmonarius*. (F) One pair of needle electrodes was inserted in the substrate without fungus as a control. (G) Fructification with inserted electrodes cut from the fructifying bag (1 day after insertion of the electrodes). (H) Raw signal recorded on the Picolog 6 software (Pico Technology Ldt). The red box represents the zoomed area shown in (I), in which we observed the effect of cutting off the fructification shown in (G). (I) Magnification of the red box from (H). Comparison of a signal for a fructification before and after cutting. Lines in blue, pink, and gray correspond to three different fructifications, while the uncolonized control corresponds to a dark violet line visible after the cut of the fruiting body in (G). After the cut, it is possible to observe the signal from the cut fruiting body (gray) resembling that of substrate control (dark violet).

[Open in new tab](https://academic.oup.com/view-large/figure/511922211/fuaf009fig2.jpg) [Download slide](https://academic.oup.com/DownloadFile/DownloadImage.aspx?image=https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/femsre/49/10.1093_femsre_fuaf009/1/fuaf009fig2.jpeg?Expires=1779996799&Signature=3Jc~By5JWQkHLIIuyllMjf1x0JlgiSwkMK1-ZxRvlhP45mxD7pDQ0fPuBMjB~IUZgQiK8zD3zJMbPtnBOOSrpNTjV73TIDe07Sjw9xmFwHO8HXjfK-KdNTzhFE5kg6XcTODSkv0AehSuNcG1mMrweGBgVXDyj-MXaep5cOchwiv48DTjQdfuLzC9AnrbTQZOoQdqBQ5l-Vt3nX1vDh2wuThlVAdMB5DxZXQxBtYDq1zNoGt9AvdIl1QvJHo-mEBlF6ffVJDqiPMHSL2Zt0dEO9GSju5eGnbNQTvSVAoOzCshwkLUmsk0H2cNh~eFQ1n7XCyBgtv~o11SS6PfIB9Zqw__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA&sec=511922211&ar=8090185&xsltPath=~/UI/app/XSLT&imagename=&siteId=5386)

Another aspect that needs to be considered in future studies for the measurement of electrical currents with macroscopic structures, at the interface of organisms, or even when using extracellular electrodes in cultures growing on solid media is the importance of the positioning of the electrodes and their reference. The electrodes used in these studies can be considered as “proximity” electrodes that record electrical field potentials. Those correspond to voltage that can arise passively from either biological (i.e. the fungus or plants) and nonbiological sources (e.g. movement of ions on a matrix), and the precise origin cannot be distinguished between these sources (Blatt et al. 2023). Moreover, the interpretation of the recorded data as action potential-like signals based on extracellular measurements of changes in voltage can be misleading. Action potentials are transmembrane potentials arising between the intracellular and extracellular space, and are generally measured with microelectrodes placed inside living cells. Instead, the use of surface and extracellular electrodes to record local voltages when placed close to or in contact with excitable cells, rather reflects synchronous behavior of multiple cells (Buzsáki et al. 2012, Blatt et al. 2024). Therefore, validating the measurements using intracellular electrodes, improving the analysis of the signal, or identifying methods to reduce the nonbiological noise is important to advance in this area.

#### Ion channels in fungi

As indicated previously, resting membrane potentials are maintained actively in the cell by controlling the movement of ions across the membrane with the help of selective channels and/or ion pumps (Martinac et al. 2008). These transmembrane proteins allow the selective movement of ions (for instance, Na <sup>+</sup>, Ca <sup>2+</sup>, and K <sup>+</sup>) across the membrane, but can also have functions other than electrical signaling (Catterall et al. 2017).

Early studies in fungal electrical signaling postulated the involvement of proton pumps (H <sup>+</sup>) and other ion channels (Ca <sup>2+</sup> and Cl <sup>−</sup>) (Slayman et al. 1976, Harold et al. 1985, Gow and Morris 1995). Spontaneous action potential-like behavior in *Neurospora* was proposed to be due to an electrogenic H <sup>+</sup> pump, or a change in the selectivity of the membrane to ions. From the various ions that were evaluated in this early study, H <sup>+</sup> and Cl <sup>−</sup> were identified as the most likely ions responsible for carrying the inward current during action potential firings (Slayman et al. 1976). Moreover, the response of spontaneous action potential-like firing activity in *A. bulbosa* and *P. ostreatus* to current injection differed from the response in classical animal models (Olsson and Hansson 1995). In these two fungi, the injection of negative currents increased the amplitude of the signals, whereas injection of negative currents inhibits the activity of neurons. This suggested that the ions and ion channels involved in the generation and maintenance of action potentials in fungi are different from those in classical animal models (Olsson and Hansson 1995). In contrast, and as indicated previously, galvanotropism and thigmotropism in *C. albicans* appear to be regulated by the movement of Ca <sup>2+</sup> via the voltage-gated channel Cch1 (Brand et al. 2007). More recently, a study in *A. nidulans* showed Ca <sup>2+</sup> signaling intracellularly in response to a localized stress. The movement of Ca <sup>2+</sup> was highly localized and caused a wave of voltage measurements with variable frequency (Itani et al. 2023).

Different types of ion and voltage-gated channels have been described in fungi based mainly on the study of yeasts. However, more recently, specific families of these channels have also been identified in filamentous fungi (Houdinet et al. 2023), including voltage-gated proton channels that displayed shared features to animal counterparts, but that were sufficiently different to confer specific functional adaptations unique to filamentous fungi (e.g. voltage range of activation or pH sensitivity) (Zhao and Tombola 2021). Moreover, the analysis of whole-genome sequencing projects allowed to identify genes likely to encode homologues of K <sup>+</sup>, Ca <sup>2+</sup>, transient receptor potential (Trp), and mitochondrial Ca <sup>2+</sup> uniporter channels (Prole and Taylor 2012). To expand this knowledge beyond pathogens, we performed a homology search for known ion and voltage-gated channels in available fungal proteomes based on human voltage-gated channel subunits (additional information is provided as the [Supplementary information](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/femsre/49/10.1093_femsre_fuaf009/1/fuaf009_supplemental_file.docx?Expires=1779996799&Signature=oYVQv9pTp8zFkRcukBto6zQDeB1JPnG5NDk~bJssGVUCqQIrxP7aU4JG2Nhory9xmiIFQwzeC3IcyzDFMaUDXF229LuPVfj~zBWvpbZvSvvJGFUAn8MeFH--ImkD9FUNVMkWc9ed5DbuC8cClhsRvVFeX36qZ6d0m0Uajmx408OR6OIguAYnSTljrAbwH7I0oMbsAQavUlxsWaWmiQw9dSco~bKJmB06mRT28YxNWz4TLdKw~gUV9Sx5aFmgua3kpRHs~D1tG6-qjPosWmLMe5fJ01Qpvw1TWAee3P9f~qjLi3AjmGgWm1A82FSVeyAqAjFL~IVN~tdmj~Y8-9atRg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)). The distribution of the hits and their presence in different fungal clades were analyzed (Fig. 3). The results of this search indicated the presence of putative voltage-gated channels in response to multiple ions (Ca <sup>2+</sup>, Cl <sup>−</sup>, K <sup>+</sup>, Na <sup>+</sup>, and H <sup>+</sup>) and the signal molecule glutamate. Most of the identified channels were present in all eight fungal phyla. However, the different subunits of the voltage-dependent K <sup>+</sup> channel KCN were less represented in Ascomycota, despite the fact that most of the proteomes screened corresponded to this phylum (1283 out of 1942 proteomes screened). In contrast, those were among the only type of channels found in Cryptomycota (three proteomes available). In Basidiomycota and Blastocladiomycota (390 and 2 proteomes screened, respectively), all the types of channels were detected, but some subunits were more common than others. In Mucoromycota and Chrytridiomycota, (84 and 23 proteomes, respectively), Cl <sup>−</sup> channels were rare (5–11 and 1, respectively). In Olpidiomycota, for which a single proteome was available, only the receptor for glutamate was detected. Finally, in Zoopagomycota, K <sup>+</sup> channels were more commonly found (details provided in the [Supplementary information](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/femsre/49/10.1093_femsre_fuaf009/1/fuaf009_supplemental_file.docx?Expires=1779996799&Signature=oYVQv9pTp8zFkRcukBto6zQDeB1JPnG5NDk~bJssGVUCqQIrxP7aU4JG2Nhory9xmiIFQwzeC3IcyzDFMaUDXF229LuPVfj~zBWvpbZvSvvJGFUAn8MeFH--ImkD9FUNVMkWc9ed5DbuC8cClhsRvVFeX36qZ6d0m0Uajmx408OR6OIguAYnSTljrAbwH7I0oMbsAQavUlxsWaWmiQw9dSco~bKJmB06mRT28YxNWz4TLdKw~gUV9Sx5aFmgua3kpRHs~D1tG6-qjPosWmLMe5fJ01Qpvw1TWAee3P9f~qjLi3AjmGgWm1A82FSVeyAqAjFL~IVN~tdmj~Y8-9atRg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)).

![Distribution of PSI-BLAST hits for homologues to voltage-gated ion channels in different fungal clades. The total number of PSI-BLAST hits with e-values < 1e-5 and the number of hits per phylum for each gene was calculated and is displayed as unstacked bar plots. The number of hits per phylum was variable.](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/femsre/49/10.1093_femsre_fuaf009/1/m_fuaf009fig3.jpeg?Expires=1779996799&Signature=j2euxdyLftTYE4HRrLT9etEoHRnjF1mtiwpU-6rXPIXnutZRAXfpm3V3ALsFptA~G6b0TQVjlv~gLWSZG7NdITpsO1uUa3Fj2Y0rREsB967jtuFztZE3Ho3dYHAbsxVROngqmAbt~Hg6k0SgUpZ2wSGljw99mta-83QHNtsuFFU5P5aexJSzxY~pR62Z5kRCTXmXx62ju7Sg9Zm7KJ4LBYpayWFBCM8T~PQdhxkcw03-cmdvuOglOiKUW3Sc8FxtE8YiDmjfmPlipMhtFarHbatOt7LzoHit~DPjreii0m5eglsZt-AuCs-EX76GiRH8ynTwzB0QmpEl5cJox6qf9w__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)

Figure 3.

Distribution of PSI-BLAST hits for homologues to voltage-gated ion channels in different fungal clades. The total number of PSI-BLAST hits with e-values < 1e-5 and the number of hits per phylum for each gene was calculated and is displayed as unstacked bar plots. The number of hits per phylum was variable.

[Open in new tab](https://academic.oup.com/view-large/figure/511922217/fuaf009fig3.jpg) [Download slide](https://academic.oup.com/DownloadFile/DownloadImage.aspx?image=https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/femsre/49/10.1093_femsre_fuaf009/1/fuaf009fig3.jpeg?Expires=1779996799&Signature=NvTCJZqkIwS7V9eB~ktCIBUcPCafNAzYo7~ddA~Rr6NH~Dod8xPHIlmerI4TchS1WsKcN2g1PeI17bK0z31lAca~VqNhXKfWdbCZKYDd2jQ8GPZIowBQNYL0JDHpIbijoYHGcIAv-k~UstY~e2RO3Cku~E~MQHcMAWq256c50dK3VxlT-3HsGEAfaEcDX7lMlrlbNQeSHVovvGgcWvG-IVUpZrlxVlKjG4GgWMw9l6L4HAcMOpWe7LDOuSSRxCrA1vW5QnG-Y7tXtYF9TeCiFzn6EwSUmibVgA~7ka4GkBr0Tkx8n7pOpM4aqlISRZN~V-z1JevUciUQQZP2ivHScg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA&sec=511922217&ar=8090185&xsltPath=~/UI/app/XSLT&imagename=&siteId=5386)

The homology search performed here suggests the widespread presence of potential ion- and voltage-gated channels in different fungal clades. However, ultimately, this type of analysis needs to be validated by structural modeling and functional characterization experiments to confirm their role on electrical signaling. The characterization of fungus-specific K <sup>+</sup> channels is an example of this type of validation (Houdinet et al. 2023). These channels were initially identified using the patch-clamp method in fungal spheroplasts and protoplasts (Gustin et al. 1986, Bertl et al. 1993). This led to the description of the *Sc* TOK1, the first member of a new family of K <sup>+</sup> channels to be described in *S. cerevisiae* (Houdinet et al. 2023). This channel was shown to elicit mainly outwardly rectifying K <sup>+</sup> currents upon membrane depolarization in yeast and when expressed in *Xenopus laevis* oocytes. This rectifying function is not directly involved in generating action potentials. Instead, it helps maintain ionic balance in yeast cells. (Gustin et al. 1986, Zhou et al. 1991, 1995, Bertl et al. 1993, Ketchum et al. 1995, Lesage et al. 1996, Loukin et al. 1997). Similar experimental studies would strongly contribute to the field.

### Evaluation of innovative recording techniques and potential improvements

In this second part of the review, we will present the evaluation of innovative recording methods that we explored to investigate electrical signaling in fungi. The goal was to expose experimental caveats that we have encountered, as well as present new methods that have the potential to provide novel evidence for electrical signaling in fungi. We hope this will promote future studies in the area and avoid costly mistakes by other researchers aiming to enter the field.

#### Resistivity measurements

Studies with giant squid neurons showed a decrease in resistance, and thus an increase in conductivity, when neurons fire action potentials (Cole and Curtis 1939). Theoretical models of action potentials, such as the Hodgkin–Huxley model, rely on changes in ion conductance (which inversely affects resistivity) across the cell membrane to describe how action potentials are generated and propagated (Häusser 2000). Although animal neurons are often used as a model, action potentials in other organisms like plants show the same 3-fold defining phases: depolarization, repolarization, and hyperpolarization. In plants, such as *Nitella flexilis*, a decrease in resistivity has also been measured during action potential events (Cole and Curtis 1938). This suggest that electrical signaling in biological systems can be often correlated with changes in resistivity. Accordingly, one way to assess the existence of action potentials in fungi is to assess a change in resistivity in the mycelium in response to stimuli. To test this, we used Mibots (Imina technology), which are piezo-driven micromanipulators that support conductivity-measurements with precise contact needle micropositioning under a camera or a microscope. The electrical measurements were performed using a Keithley 2400 source meter for the recording of current–voltage data. Three different fungi were tested: *Fusarium oxysporum, C. cinerea*, and *P. ostreatus* (Fig. 4). Conductivity was measured using the piezoelectric actuators connected in the Mibots (Fig. 4A and B). These piezoelectric actuators were used to measure resistance on indium tin oxide (ITO) stripes on uninoculated glass slides (Fig. 4C) or on slides on which the fungi were grown (Fig. 4D). Resistance can be measured by placing the actuators on the same stripe at variable distances (e.g. Fig. 4C). In the uninoculated glass slide covered with ITO stripes, the resistance was between 45 and 128 ohms, depending on the distance at which the actuators were placed (distance in mm indicated in Fig. 4E). In contrast, in the glass slides colonized by the three fungi, the presence of the mycelium resulted in an increase in resistance (Fig. 4E). In the case of the mycelium of *F. oxysporum*, a resistance value could be obtained in a variable number of stripes (seven ITO stripes per slide as shown in Fig. 4C) in four independent tests. In the case of slides colonized by *C. cinerea* and *P. ostreatus*, the resistance was so high that measurements could only be obtained in the last stripe that contained the lowest biomass (resistance above 5 × 10 <sup>8</sup> ohms; Fig. 4E). We ascribed the increase in resistance to the growth of the mycelium on the ITO stripes and the resulting insulation from the production of hydrophobins, as has been suggested previously (Gow and Morris 1995). Therefore, this method, which was easy to implement, could be used in the future to evaluate the effect of components of the cell wall on insulation and to validate the role of cell wall components on preventing ion leakage (Morell and Quarles 1999). For this, future experiments could employ mutants devoid of a cell wall such as the *N. crassa* slime mutant (Levina et al. 2002) or diverse *Penicillium expansum* mutant strains that lack hydrophobins (Luciano-Rosario et al. 2022). The use of such mutants should circumvent the measurement impairments thought to be caused by the cell wall and prove its role as an insulator. Mycelial growth in the slime mutant can be challenging, but a combination of this type of recording method with the use of, for instance, microfluidic devices to provide structural support could help to circumvent this issue.

![Conductivity measurement of fungal mycelia with MiBots (Imina technologies): for this experiment, we tested F. oxysporum, P. ostreatus, and C. cinerea. The three fungi were cultivated on malt agar medium, where glass slides covered by stripes of ITO were placed next to the inoculum. Once the fungus had grown onto the slide, it was placed onto the MiBots arena to conduct measurements. (A) Camera system mounted in order to visualize the probes for more accurate measurements with the MiBots piezoelectric actuators. (B) Example of a measurement on a slide colonized by F. oxysporum hyphae. (C) Details of ITO-covered glass slide. The ITO stripes are transparent and therefore, a mask is placed underneath to indicate their position and to guide the measurements. The position of the ITO stripes corresponds to the middle lines in the three-line marks highlighted by the numbers 1–7. The slide is about 2.5 cm × 2.5 cm, with the stripes being separated by around 2 mm. In the top left part, there is a rectangular area covered by ITO that can be used as a positive control. In this example, the distance between the electrode probes, positioned using the piezoelectric actuators, corresponds to 12 mm. (D) Example of measurement on stripe 7 on a slide colonized by P. ostreatus. (E) Plotting of the resistance measurements (logarithmic Ohm—for the detailed measurements, please see the Supplementary information). The controls correspond to measurements in an uninoculated slide on stripe 1 with the electrodes positioned at different distances along the stripe (2 mm, 4 mm, 6 mm, 8 mm, and 12 mm, respectively). For F. oxysporum, four individual slides were measured and only the values on the stripes that could be measured are reported in different stripes. For C. cinerea and P. ostreatus, recordings were only possible on stripe 7.](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/femsre/49/10.1093_femsre_fuaf009/1/m_fuaf009fig4.jpeg?Expires=1779996799&Signature=kN7h7i0ZUqTMSXow5JxeZG3u2mohWI7mbipn10yk7vb0Ndd85IqYChy5yghqH4RAa46YyhtUM7o05Gjxho1kyFmirL2c6azrJuXBVxG1dNXyELgxaDsJmsTO3IFE8RJ8U3~6oyeO2DksdMAJHNaUpAvDU36mVkR9yF5ox7eQG8SKhmh1TTEd9Soc0cJeLs0fyo-bNUDyvW-ROcelVDT4LpB826NjfpcQ3~dqAgvUU-AGXWZPGU877was82dcY7uGsAkb3gul~g9gcrt0mppL78AJLgjTCwzRJk2NHx6ng5gft0UlQG9OJyKLOO1CMiZhkxrvqna2f1aRYFys51uTMA__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)

Figure 4.

Conductivity measurement of fungal mycelia with MiBots (Imina technologies): for this experiment, we tested *F. oxysporum, P. ostreatus*, and *C. cinerea*. The three fungi were cultivated on malt agar medium, where glass slides covered by stripes of ITO were placed next to the inoculum. Once the fungus had grown onto the slide, it was placed onto the MiBots arena to conduct measurements. (A) Camera system mounted in order to visualize the probes for more accurate measurements with the MiBots piezoelectric actuators. (B) Example of a measurement on a slide colonized by *F. oxysporum* hyphae. (C) Details of ITO-covered glass slide. The ITO stripes are transparent and therefore, a mask is placed underneath to indicate their position and to guide the measurements. The position of the ITO stripes corresponds to the middle lines in the three-line marks highlighted by the numbers 1–7. The slide is about 2.5 cm × 2.5 cm, with the stripes being separated by around 2 mm. In the top left part, there is a rectangular area covered by ITO that can be used as a positive control. In this example, the distance between the electrode probes, positioned using the piezoelectric actuators, corresponds to 12 mm. (D) Example of measurement on stripe 7 on a slide colonized by *P. ostreatus*. (E) Plotting of the resistance measurements (logarithmic Ohm—for the detailed measurements, please see the [Supplementary information](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/femsre/49/10.1093_femsre_fuaf009/1/fuaf009_supplemental_file.docx?Expires=1779996799&Signature=oYVQv9pTp8zFkRcukBto6zQDeB1JPnG5NDk~bJssGVUCqQIrxP7aU4JG2Nhory9xmiIFQwzeC3IcyzDFMaUDXF229LuPVfj~zBWvpbZvSvvJGFUAn8MeFH--ImkD9FUNVMkWc9ed5DbuC8cClhsRvVFeX36qZ6d0m0Uajmx408OR6OIguAYnSTljrAbwH7I0oMbsAQavUlxsWaWmiQw9dSco~bKJmB06mRT28YxNWz4TLdKw~gUV9Sx5aFmgua3kpRHs~D1tG6-qjPosWmLMe5fJ01Qpvw1TWAee3P9f~qjLi3AjmGgWm1A82FSVeyAqAjFL~IVN~tdmj~Y8-9atRg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)). The controls correspond to measurements in an uninoculated slide on stripe 1 with the electrodes positioned at different distances along the stripe (2 mm, 4 mm, 6 mm, 8 mm, and 12 mm, respectively). For *F. oxysporum*, four individual slides were measured and only the values on the stripes that could be measured are reported in different stripes. For *C. cinerea* and *P. ostreatus*, recordings were only possible on stripe 7.

[Open in new tab](https://academic.oup.com/view-large/figure/511922223/fuaf009fig4.jpg) [Download slide](https://academic.oup.com/DownloadFile/DownloadImage.aspx?image=https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/femsre/49/10.1093_femsre_fuaf009/1/fuaf009fig4.jpeg?Expires=1779996799&Signature=kS8kvESztunS6WPgQAOcKVqS7PxJsYKJWX46H2Hu5FGWL9a6SQ3KGF8QYs95qBbK06fO~D7b0nkigBDZA6RRsC~fR9iV2CByzVL30~QFszVtud~UWupl9yN6sc~oeXCXzA552-iFA3XRRs9zOETDNq~MOR~bObx1fCVsJnGgWVStvrdwrbWWcIbQD74PrJn4PUjPRKSOb1JeRpzWAA3H3EfnJf2hnkd6txEWDTqoIamWGLNKz~RfUrtUBzFJjn6ywUMr1mwfxbCrU7czNn8xLUpttbH-tQ1fp3PgwKh0guYnak9cVRYw~O61lBmvomJGNUzB5cOqp57Y~Eiioc1PfQ__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA&sec=511922223&ar=8090185&xsltPath=~/UI/app/XSLT&imagename=&siteId=5386)

#### Multielectrode arrays

Studies in human neuronal networks have led to recent technical advancements that allow the extracellular recording of voltage fluctuations. The use of a similar approach for mycelial networks could confirm previous results from vibrating microelectrodes where external currents were measured around the apex (Stump et al. 1980, Horwitz et al. 1984). We attempted this by using a high-density multielectrode array (MEA) from 3Brain ([3Brain.com](https://www.3brain.com/), Switzerland) developed to record electrical activity of neuronal networks *in vitro*. The MEA microchip consists of an array of more than 4000 electrodes of micrometer size (20 × 20 μm <sup>2</sup> sensing area, 80 μm pitch) that register voltage fluctuations with a sensitivity of few tens of µV (Fig. 5A and B). The voltage fluctuations result from extracellular ionic flows occurring when ion channels and transporters of the cell membrane open. The signals collected simultaneously by each of the thousands of electrodes can be visualized as functional activity images, allowing for tracking of electrical impulses propagating inside an electrogenic tissue with micrometer resolution. Multiple tests for recording the propagation of electrical impulses in a mycelial network were conducted using *F. oxysporum*. First, the fungus was inoculated by placing a small agar plug on the surface of liquid medium overlying the electrodes. This method did not yield any results because the fungus grew on the surface of the medium at the air–medium interface and never made physical contact with the electrodes. Therefore, we developed a second inoculation method (Buffi et al. 2023), to be able to place and cultivate the fungus directly onto the chip’s surface (Fig. 5C–E). This second approach resulted in a recording. An oscillation signal in the range of ± 50 µV was recorded. However, the signal remained constant after induction with a calcium ionophore, which is known to induce a physiological reaction in *F. oxysporum* (Hoshino et al. 1991). Also, killing the fungus with the antifungal agent cycloheximide did not affect the signal. Upon discussion with the chip developers, it became evident that the signal recorded corresponded to background noise. MEA chips were originally designed to measure relatively high frequency signals (from 5–10 to 2–3k Hz), while in most of the existing literature, fungal signals have temporal dynamics of tens of seconds up to hours resulting in a signal spectral frequency in the order of 0.0003–0.1 Hz. This major difference makes the recording using the commercial chip design inappropriate and would require major modifications of the design and the analysis software to be suitable. Nevertheless, this type of electrode array could provide a way to measure the propagation of an electrical signal within the complex spatial structure of a growing mycelium.

![Measuring voltage fluctuations in a mycelial network using a high-density MEA from 3Brain. (A) MEA chip used (~1 cm2). The microchip (gold square in the middle) is surrounded by a plastic container acting as a reservoir for medium and organism growth. (B) Close-up image of the microchip chamber. The chip contains 4096 electrodes for measuring electrical activity. On the sides, the two large gold electrodes (outside the chip) act as references for the differential measurement. (C) Image showing the growth of F. oxysporum inoculated using the spore drop method in Dulbecco’s modified eagle medium (DMEM; GiBCO) liquid medium. Image taken 2 days postinoculation. (D) Fusarium oxysporum at 3 days postinoculation (before measurements). For the measurements, the chamber (B) was flooded with medium (required for the measurements). (E) Magnified image showing F. oxysporum hyphae that have grown from the point of inoculation and are attached to the electrodes.](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/femsre/49/10.1093_femsre_fuaf009/1/m_fuaf009fig5.jpeg?Expires=1779996799&Signature=ZTW~lr3Lq7bzc3AqDlSyNviN8MVMwPfznoSte6mUYv2Eol6vzee8LJyfb8k9Gj9dG46N9ZbuYjno-wR2SKQVO8A7L9nrpokfWIOhFNRUHPLPT2jDwqP~k-N1fIPRkGhBjrksdIucP7RzWKxnmig-3KuB0FAFoZXhE5h~cAkykP6~4jYXWzOnw~k9tFyXPxWj9BIg6HS1~iabbERLSUMhYBQyzW0oRcwtyEF6oIL6WISnapGqWFMLY8I9bzuEi7xyP69RjR4IXWXvuk6Jyv1FWFUOAGq3holfcAUfKaB4zD7pqk0D0-QfUMIrdUAXpLpCcFWM1kF~aSq7gf7~IlhZNg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)

Figure 5.

Measuring voltage fluctuations in a mycelial network using a high-density MEA from 3Brain. (A) MEA chip used (~1 cm <sup>2</sup>). The microchip (gold square in the middle) is surrounded by a plastic container acting as a reservoir for medium and organism growth. (B) Close-up image of the microchip chamber. The chip contains 4096 electrodes for measuring electrical activity. On the sides, the two large gold electrodes (outside the chip) act as references for the differential measurement. (C) Image showing the growth of *F. oxysporum* inoculated using the spore drop method in Dulbecco’s modified eagle medium (DMEM; GiBCO) liquid medium. Image taken 2 days postinoculation. (D) *Fusarium oxysporum* at 3 days postinoculation (before measurements). For the measurements, the chamber (B) was flooded with medium (required for the measurements). (E) Magnified image showing *F. oxysporum* hyphae that have grown from the point of inoculation and are attached to the electrodes.

[Open in new tab](https://academic.oup.com/view-large/figure/511922226/fuaf009fig5.jpg) [Download slide](https://academic.oup.com/DownloadFile/DownloadImage.aspx?image=https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/femsre/49/10.1093_femsre_fuaf009/1/fuaf009fig5.jpeg?Expires=1779996799&Signature=Pc8xA16Q42VW8w~wC-Oiz19Is0mFC5zyTOQ4VfnNdJeokaWQjqe3RIeGhJexNpKo5kitvFIc4Nz8SdJQAU96u349t2LapIVj40qD41dr63e0-olnssJ1QEHD9NWGsTiAcr7BLZQ4E4LQociBaoncR6g1VgfcXvy5xf48Jix0FdPRwq2-XNGZpYwUzM5H2VSxsMjccrfKJJAPLBc6QOT7ptkVy7RSeJ3Z1-eHOfwQCXh6SZn6yvnHF6Dg3qf8wqJFFMgxt6tNuvCAbrDiJpR2wYFASGXI0YLR3fkLutHAPSvQ2ISQF~MgwqNvaiTp4RHs2Dq1eyIs6YRztp05AbUp~w__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA&sec=511922226&ar=8090185&xsltPath=~/UI/app/XSLT&imagename=&siteId=5386)

#### Visualization of membrane potentials using dyes

The last method tested here aimed to visualize changes in membrane potential in fungal hyphae by coupling the use of voltage sensitive dyes with fluorescence microscopy. Voltage sensitive dyes are molecules that bind to the cell membrane and whose fluorescence changes when a membrane potential fluctuation is detected (Fig. 6A). They have been mainly used for imaging of complex neuronal network behaviors (Ebner and Chen 1995, Chemla and Chavane 2010, Adams and Levin 2012, Kulkarni and Miller 2017). Thioflavin T (ThT) is a fluorescent dye usually used for staining amyloid fibrils (Biancalana and Koide 2010) that was previously used as a membrane potential dye for bacteria (Prindle et al. 2015). ThT does not cross the plasma membrane. The dye is positively charged and accumulates close to the membrane in response to changes in membrane potential (for instance if the plasma membrane becomes negatively charged). This makes ThT a good candidate for slow membrane potential changes. To test this, *F. oxysporum* was cultivated in liquid medium to which ThT was added at a final concentration of 30 µM (Fig. 6B). In the microscopic images, an uneven staining along hyphae and on spores was observed (Fig. 6C). Moreover, it was very difficult to distinguish between changes in staining resulting from variations in membrane potential or simply diffusion of the dye. Therefore, optimization of the set-up is required including additional controls to test photobleaching or the comparison of alive versus dead hyphae. Combining fungal staining and cultivation on microfluidic devices would help confine single hyphae, thus eliminating issues related to hyphal superposition. Microfluidic devices have been used in the past in order to spatially separate single hyphae and observe different physiological interactions (Stanley et al. 2016). Microfluidic devices have emerged particularly valuable tools for studying hyphal growth dynamics, spore germination, and fungal network formation with spatial and temporal resolution (Richter et al. 2022). Although the compartments of the microfluidic devices are usually saturated with liquid medium, potentially impairing measurements, the use of the devices without fluid is also possible (Gimeno et al. 2021). Alternatively, the use of other methods for visualizing the hyphal network such as the drop method (Buffi et al. 2023) could be another possible solution.

![Visualization of membrane potential changes with the voltage sensitive dye ThT. (A) Scheme representing the mechanism behind the visualization of membrane potential using ThT. ThT is positively charged but it does not cross the fungal membrane. If the inner cell is negatively charged (e.g. efflux of positively charged ions), ThT will concentrate on the surface of the cell and fluorescence can then be detected (image in the bottom of the scheme). This can be the result of changes in the movement of specific ions across the membrane. (B) Fusarium oxysporum growing in Vogel-N-Medium in a 24-well cell culture plate (Corning incorporated). ThT was added in a final concentration of 30 µM, the plate was covered with dark paper and mixed gently for half an hour before performing imaging on an inverted microscope (EVOS FL imaging system, Invitrogen) with a DAPI filter. (C) Example of a picture overlying a DAPI image with a bright field image showing the inconsistent staining with ThT. Here part of the mycelium and spores of F. oxysporum were stained while others were not. Furthermore, the issue of imaging superposed stained hyphae can be observed.](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/femsre/49/10.1093_femsre_fuaf009/1/m_fuaf009fig6.jpeg?Expires=1779996799&Signature=noIU-wrQ7KF-42aDC2diN1TkEbar8tMPnGwMn~U7gTRHKPw3-aCmW2BKYlXwMhquE~fxEI-sZNsLbwe2jJ3eQbs4qsQu94snxuv~opQeubizIrQ6yP8UErjx6tDeJkOlrsMuliRzvNTMtAG06w5cGPYWjkYqwetVA4rKFTex7lAiUkA8PmR6zk7MwM7Yj0ashToBxNtltTZeBewplqRjcgUPRPpRDLKRM3tPMZDCN6Pn8UcJsjSzQZq4irGemoouTfYPaOFS22ujR98ITQl109fiEymqvY036hYSR7-vLYsSbCdCIJnoHz3G0vOxo6lxMrc5K0jBGD6bx~4fSqoBbw__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)

Figure 6.

Visualization of membrane potential changes with the voltage sensitive dye ThT. (A) Scheme representing the mechanism behind the visualization of membrane potential using ThT. ThT is positively charged but it does not cross the fungal membrane. If the inner cell is negatively charged (e.g. efflux of positively charged ions), ThT will concentrate on the surface of the cell and fluorescence can then be detected (image in the bottom of the scheme). This can be the result of changes in the movement of specific ions across the membrane. (B) *Fusarium oxysporum* growing in Vogel-N-Medium in a 24-well cell culture plate (Corning incorporated). ThT was added in a final concentration of 30 µM, the plate was covered with dark paper and mixed gently for half an hour before performing imaging on an inverted microscope (EVOS FL imaging system, Invitrogen) with a DAPI filter. (C) Example of a picture overlying a DAPI image with a bright field image showing the inconsistent staining with ThT. Here part of the mycelium and spores of *F. oxysporum* were stained while others were not. Furthermore, the issue of imaging superposed stained hyphae can be observed.

[Open in new tab](https://academic.oup.com/view-large/figure/511922229/fuaf009fig6.jpg) [Download slide](https://academic.oup.com/DownloadFile/DownloadImage.aspx?image=https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/femsre/49/10.1093_femsre_fuaf009/1/fuaf009fig6.jpeg?Expires=1779996799&Signature=So1YoiV6pfSt00S04ZXGaOROg~ccGsnIxDSjt~BIP-C5p8xVq1I-bfHr-6IW9cSGduBADsEvzn0Lv8aRwyRxi25ealUp628sn70PpmXKuPUClDbQIyWMY-OJQDYqPz8SU~q3hHiTqwv7uyTlPvbYDrnCDj9dnrvxBhaE25A4KeHF4AQrZF~MHqUNJHgsWyl9hmur-LpNTK19YIoLBfOCRL7D30IttnbvWs-4zrZcNgTdR2NOOUzYQcbjOOm-6KZPfa0GCGgEH9zUWklDyNKbZPJWfVXx7w-WmSyiXtb8h-KgULxWNzLI1Is8uH2AkbCP4TO7pZQrsWOOUcTdaQp1hg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA&sec=511922229&ar=8090185&xsltPath=~/UI/app/XSLT&imagename=&siteId=5386)

## Future directions

The challenges encountered so far underscore the complexity of accurately recording electrical signals in fungi. A recurrent challenge in the experimental systems described and evaluated above is the difficulty in effectively measuring electrical signals intra- or extracellularly due to the fungal cell wall. This obstacle is not unique to fungi; similar issues were encountered in plant studies. For intracellular measurements, this issue was partially overcome by using aphid stylets as probes for plants (Tjallingii 1985). However, translating this approach to fungi (for instance, using nematode stylets) could pose significant technical challenges due to the small size of individual hyphae. The use of internal microelectrodes in fungi has raised concerns about altering fungal behavior, such as causing membrane leakage, but new methods provide alternatives to those. For instance, the injection of nanopebbles coupled with a voltage sensitive dye (Koo Lee and Kopelman 2012) could be used to measure intracellular ionic currents. Nanopebbles are nanoparticles composed of an external inert coating and an active inner sensor that can be visualized by microscopy without interfering with the cell functioning. The injection of nanopebbles in fungal mycelia could be achieved using a microfluidic probe connected to an atomic force microscope (FluidFM). This approach has been used for instance to inject bacteria into fungal cells (Guillaume-Gentil et al. 2022, Giger et al. 2024), and could be used to inject the nanopebbles or to create ionic fluxes and investigate the propagation of an electrical signal in the mycelial network. Another approach involves the expression of intracellular reporters for specific ions such as Ca <sup>2+</sup>. Indeed, the expression of genetically encoded Ca <sup>2+</sup> indicators has been shown for different unicellular and multicellular fungi, but it is still challenging to achieve and optimize (Carbó et al. 2017, Barykina et al. 2020, Kim et al. 2021). The potential application of this technology for signaling in fungal composite materials has been recently reviewed elsewhere (Schyck et al. 2024).

Future research might also benefit from exploring innovative approaches, such as genetically encoded voltage indicators (GEVI) (Yang and St-Pierre 2016). Such fluorescent proteins could provide a less invasive way of tracking changes in membrane potential, similar to techniques used in neuronal studies. For this, identifying good models is crucial. For instance, *C. cinerea* (a saprotrophic fungus), which has served as a model organism for homobasidiomycete fungi, is a good candidate to study the effect of electrical signaling during fruiting body formation (Navarro-González et al. 2011). Moreover, this fungus is amenable to genetic manipulation and it has been modified to express fluorescent metabolic reporters in response to biotic stress like nematode attacks (Schmieder et al. 2019). By expressing voltage-sensitive fluorescent proteins in *C. cinerea* and coupling this with fluorescently marked analogues (e.g. 2-NBDG glucose or labeled phosphorus and carbon), electrical signaling could be coupled to physiological and behavioral responses. Such an approach could reveal how fungi coordinate mycelial responses to biological (e.g. attacks by mycoparasitic fungi or nematodes) or abiotic (e.g. fruiting body formation in response to electrical signals) stimuli. Furthermore, finding a good model organism could help further improve the use of GEVI in complex networks with low voltage changes.

## Conclusion

Demonstrating the biological origin of electrical signals and improving our understanding of the mechanisms and roles of electrical communication in fungi has implications reaching beyond mycology. For instance, parallels and differences have been highlighted as part of the polar growth and intracellular communication of neurons and hyphae, in which mutual progress can lead, for instance, to a better understanding of mechanisms of neural diseases. Reciprocally, neurons could serve as a model to study tip-to-nucleus communication in hyphae (Etxebeste and Espeso 2016). In ecology, it could reshape our understanding of fungal physiology and interactions with other organisms. This has implications in diverse areas and can provide new ways to tackle the emerging problem of fungal diseases in both agriculture and medicine (Rickerts 2019, Fisher et al. 2022, The Lancet Infectious Diseases 2023). Moreover, in the field of biotechnology, leveraging fungal electrical properties could pave the way for innovative applications, such as the use of fungi in biosensors or as components in biological computing systems (Adamatzky 2018b).

## Funding

This research was supported by a Science Focus Area Grant from the U.S. Department of Energy (DOE), Biological and Environmental Research (BER), Biological System Science Division (BSSD) under the grant number LANLF59T to P.S.C. and the Swiss National Science Foundation grant 310030\_212435 to M.K.

## Acknowledgments

We would like to thank Gilles Weder and Sarah Heub (CSEM), and Alessando Maccione ([3Brain.com](https://www.3brain.com/)) for their help during the experiments with MEA chips.

## Conflict of interest

None declared.

## References

Abadeh

A

,

Lew

RR

..

Microbiology

.

2013

;

159

:

2386

–

94

.

[10.1099/MIC.0.071191-0/CITE/REFWORKS](https://doi.org/10.1099/MIC.0.071191-0/CITE/REFWORKS)

.

Adamatzky

A

,

Gandia

A

..

Biophys Rev Lett

.

2021

;

16

:

133

–

41

.

[10.1142/S1793048021500089](https://doi.org/10.1142/S1793048021500089)

.

Adamatzky

A

..

R Soc Open Sci

.

2022

;

9

.

[10.1098/RSOS.211926](https://doi.org/10.1098/RSOS.211926)

.

Adams

DS

,

Levin

M

..

Cold Spring Harb Protoc

.

2012

;

2012

:

459

–

64

.

Armbruster

BL

,

Weisenseel

MH

..

Protoplasma

.

1983

;

115

:

65

–

69

.

[10.1007/BF01293582](https://doi.org/10.1007/BF01293582)

.

Ashford

AE

,

Allaway

WG

.. In:

Biology of the Fungal Cell

.

Berlin

:

Springer

,

2007

,

49

–

86

.

[10.1007/978-3-540-70618-2\_2](https://doi.org/10.1007/978-3-540-70618-2_2)

.

Ayling

SM

,

Smith

SE

,

Smith

FA

..

New Phytologist

.

2000

;

147

:

631

–

9

.

Barykina

NV

,

Sotskov

VP

,

Gruzdeva

AM

et al..

Int J Mol Sci

.

2020

;

21

:

3012

.

[10.3390/IJMS21083012](https://doi.org/10.3390/IJMS21083012)

.

Berbara

RLL

,

Morris

BM

,

Fonseca

HMAC

et al..

New Phytol

.

1995

;

129

:

433

–

8

.

[10.1111/J.1469-8137.1995.TB04314.X](https://doi.org/10.1111/J.1469-8137.1995.TB04314.X)

.

Bertl

A

,

Slayman

CL

,

Gradmann

D

..

J Membr Biol

.

1993

;

132

:

183

–

99

.

[10.1007/BF00235737/METRICS](https://doi.org/10.1007/BF00235737/METRICS)

.

Biancalana

M

,

Koide

S

..

Biochim Biophys Acta Proteins Proteomics

.

2010

;

1804

:

1405

–

12

.

Blatt

MR

,

Draguhn

A

,

Taiz

L

et al..

Plant Signal Behav

.

2023

;

18

.

[10.1080/15592324.2023.2222957](https://doi.org/10.1080/15592324.2023.2222957)

.

Blatt

MR

,

Pullum

GK

,

Draguhn

A

et al..

Fungal Ecol

.

2024

;

68

:

101326

.

[10.1016/J.FUNECO.2023.101326](https://doi.org/10.1016/J.FUNECO.2023.101326)

.

Böhm

J

,

Scherzer

S

,

Krol

E

et al..

Curr Biol

.

2016

;

26

:

286

–

95

.

[10.1016/j.cub.2015.11.057](https://doi.org/10.1016/j.cub.2015.11.057)

.

Boschker

HTS

,

Cook

PLM

,

Polerecky

L

et al..

Nat Commun

.

2021

;

12

:

1

–

12

.

[10.1038/s41467-021-24312-4](https://doi.org/10.1038/s41467-021-24312-4)

.

Brand

A

,

Gow

NAR

..

Curr Opin Microbiol

.

2009

;

12

:

350

.

[10.1016/J.MIB.2009.05.007](https://doi.org/10.1016/J.MIB.2009.05.007)

.

Brand

A

,

Shanks

S

,

Duncan

VMS

et al..

Curr Biol

.

2007

;

17

:

347

–

52

.

[10.1016/j.cub.2006.12.043](https://doi.org/10.1016/j.cub.2006.12.043)

.

Brenner

ED

,

Stahlberg

R

,

Mancuso

S

et al..

Trends Plant Sci

.

2006

;

11

:

413

–

9

.

Brette

R.

,

Destexhe

A.

.. In:

Brette

R.

,

Destexhe

A.

(Eds.),

Intracellular recording

.

Cambridge

:

Cambridge University Press

,

2012

,

44

–

91

.

Buffi

M

,

Cailleau

G

,

Kuhn

T

et al..

MicroLife

.

2023

;

4

:

1

–

13

.

[10.1093/FEMSML/UQAD042](https://doi.org/10.1093/FEMSML/UQAD042)

.

Buzsáki

G

,

Anastassiou

CA

,

Koch

C

..

Nat Rev Neurosci

.

2012

;

13

:

407

–

20

.

[10.1038/nrn3241](https://doi.org/10.1038/nrn3241)

.

Canales

J

,

Henriquez-Valencia

C

,

Brauchi

S

..

Front Plant Sci

.

2018

;

8

.

[10.3389/fpls.2017.02173](https://doi.org/10.3389/fpls.2017.02173)

.

Carbó

N

,

Tarkowski

N

,

Ipiña

EP

et al..

Mol Biol Cell

.

2017

;

28

:

501

.

[10.1091/MBC.E16-07-0481](https://doi.org/10.1091/MBC.E16-07-0481)

.

Catterall

WA

,

Wisedchaisri

G

,

Zheng

N

..

Nat Chem Biol

.

2017

;

13

:

455

.

[10.1038/NCHEMBIO.2353](https://doi.org/10.1038/NCHEMBIO.2353)

.

Chemla

S

,

Chavane

F

..

J Physiol

.

2010

;

104

:

40

–

50

.

Clarke

D

,

Whitney

H

,

Sutton

G

et al..

Science

.

2013

;

340

:

66

–

69

.

Cole

KS

,

Curtis

HJ

..

J Gen Physiol

.

1938

;

22

:

37

–

64

.

[10.1085/JGP.22.1.37](https://doi.org/10.1085/JGP.22.1.37)

.

Cole

KS

,

Curtis

HJ

..

J Gen Physiol

.

1939

;

22

:

649

–

70

.

Curtis

HJ

,

Cole

KS

..

J Cell Comp Physiol

.

1942

;

19

:

135

–

44

.

Darrah

PR

,

Tlalka

M

,

Ashford

A

et al..

Eukaryot Cell

.

2006

;

5

:

1111

–

25

.

10.1128

.

Dorn

A

,

Weisenseel

MH

..

Protoplasma

.

1982

;

113

:

89

–

96

.

[10.1007/BF01281996](https://doi.org/10.1007/BF01281996)

.

Ebner

TJ

,

Chen

G

..

Prog Neurobiol

.

1995

;

46

:

463

–

506

.

Etxebeste

O

,

Espeso

EA

..

FEMS Microbiol Rev

.

2016

;

40

:

610

–

24

.

[10.1093/FEMSRE/FUW021](https://doi.org/10.1093/FEMSRE/FUW021)

.

Fischer

MS

,

Glass

NL

..

Front Microbiol

.

2019

;

10

.

[10.3389/fmicb.2019.00619](https://doi.org/10.3389/fmicb.2019.00619)

.

Fisher

MC

,

Alastruey-Izquierdo

A

,

Berman

J

et al..

Nat Rev Microbiol

.

2022

;

20

:

557

–

71

.

[10.1038/s41579-022-00720-1](https://doi.org/10.1038/s41579-022-00720-1)

.

Fricker

M

,

Boddy

L

,

Bebber

D

.. In:

Howard

RJ

,

Gow

NAR

(eds),

Biology of the Fungal Cell

.

Berlin

:

Springer

,

2007

,

309

–

30

.

[10.1007/978-3-540-70618-2\_13](https://doi.org/10.1007/978-3-540-70618-2_13)

.

Fricker

MD

,

Heaton

LLM

,

Jones

NS

et al.. In:

The Fungal Kingdom

.

Washington, DC

:

American Society of Microbiology

,

2017

.

[10.1128/microbiolspec.FUNK-0033-2017](https://doi.org/10.1128/microbiolspec.FUNK-0033-2017)

.

Fukasawa

Y

,

Akai

D

,

Takehi

T

et al..

Sci Rep

.

2024

;

14

:

1

–

7

.

[10.1038/s41598-024-66223-6](https://doi.org/10.1038/s41598-024-66223-6)

.

Garrill

A

,

Davies

JM

..

Mycol Res

.

1994

;

98

:

257

–

63

.

[10.1016/S0953-7562(09)80452-8](https://doi.org/10.1016/S0953-7562\(09\)80452-8)

.

Garrill

A

,

Jackson

SL

,

Lew

RR

et al..

Eur J Cell Biol

.

1993

;

60

:

358

–

65

. [http://europepmc.org/abstract/MED/7687216](http://europepmc.org/abstract/MED/7687216).

Garrill

A

,

Lew

RR

,

Heath

IB

..

J Cell Sci

.

1992

;

101

:

721

–

30

.

[10.1242/JCS.101.3.721](https://doi.org/10.1242/JCS.101.3.721)

.

Giger

GH

,

Ernst

C

,

Richter

I

et al..

Nature

.

2024

;

635

:

415

–

22

.

[10.1038/s41586-024-08010-x](https://doi.org/10.1038/s41586-024-08010-x)

.

Gilbert

L

,

Johnson

D

.. In:

Advances in Botanical Research

. Vol.

82

,

Amsterdam

:

Elsevier

,

2017

,

83

–

97

.

Gimeno

A

,

Stanley

CE

,

Ngamenie

Z

et al..

Commun Biol

.

2021

;

4

:

1

–

10

.

[10.1038/s42003-021-01767-1](https://doi.org/10.1038/s42003-021-01767-1)

.

Gow

NAR

,

Morris

BM

..

Botan J Scot

.

1995

;

47

:

263

–

77

.

[10.1080/03746609508684833](https://doi.org/10.1080/03746609508684833)

.

Guillaume-Gentil

O

,

Gäbelein

CG

,

Schmieder

S

et al..

Commun Biol

.

2022

;

5

:

1

–

10

.

[10.1038/s42003-022-03127-z](https://doi.org/10.1038/s42003-022-03127-z)

.

Gustin

MC

,

Martinac

B

,

Saimi

Y

et al..

Science

.

1986

;

233

:

1195

–

7

.

[10.1126/SCIENCE.2426783](https://doi.org/10.1126/SCIENCE.2426783)

.

Hamill

OP

,

Marty

A

,

Neher

E

et al..

Pflügers Archiv

.

1981

;

391

:

85

–

100

.

[10.1007/BF00656997](https://doi.org/10.1007/BF00656997)

.

Harold

FM

,

Kropf

DL

,

Caldwell

JH

..

Exp Mycol

.

1985

;

9

:

3

–

86

.

[10.1016/0147-5975(85)90013-1](https://doi.org/10.1016/0147-5975\(85\)90013-1)

.

Heaton

L

,

Obara

B

,

Grau

V

et al..

Fungal Biol Rev

.

2012

;

26

:

12

–

29

.

[10.1016/J.FBR.2012.02.001](https://doi.org/10.1016/J.FBR.2012.02.001)

.

Horwitz

BA

,

Weisenseel

MH

,

Dorn

A

et al..

Plant Physiol

.

1984

;

74

:

912

–

6

.

[10.1104/pp.74.4.912](https://doi.org/10.1104/pp.74.4.912)

.

Hoshino

T

,

Mizutani

A

,

Shimizu

S

et al..

J Biochem

.

1991

;

110

:

457

–

61

.

[10.1093/oxfordjournals.jbchem.a123602](https://doi.org/10.1093/oxfordjournals.jbchem.a123602)

.

Houdinet

G

,

Guerrero-Galán

C

,

Rose

BD

et al..

Trends Microbiol

.

2023

;

31

:

511

–

20

.

[10.1016/j.tim.2022.11.007](https://doi.org/10.1016/j.tim.2022.11.007)

.

Hutchings

MJ

,

Wijesinghe

DK

,

John

EA

.. In:

The Ecological Consequences of Environmental Heterogeneity

.

Cambridge

:

Cambridge University Press

,

2000

,

91

–

109

.

Hyde

KD

,

Baldrian

P

,

Chen

Y

et al..

Fungal Diver

.

2024

;

125

:

1

–

71

.

[10.1007/S13225-023-00532-5](https://doi.org/10.1007/S13225-023-00532-5)

.

Itani

A

,

Masuo

S

,

Yamamoto

R

et al..

PNAS Nexus

.

2023

;

2

:

1

–

10

.

[10.1093/PNASNEXUS/PGAD012](https://doi.org/10.1093/PNASNEXUS/PGAD012)

.

Jaffe

LF

,

Nuccitelli

R

..

J Cell Biol

.

1974

;

63

:

614

–

28

.

[10.1083/jcb.63.2.614](https://doi.org/10.1083/jcb.63.2.614)

.

Jaffe

MJ

,

Leopold

AC

,

Staples

RC

..

Am J Bot

.

2002

;

89

:

375

–

82

.

James

TY

,

Stajich

JE

,

Hittinger

CT

et al..

Annu Rev Microbiol

.

2020

;

74

:

291

–

313

.

[10.1146/ANNUREV-MICRO-022020-051835/1](https://doi.org/10.1146/ANNUREV-MICRO-022020-051835/1)

.

Jia

N

,

Yang

J

,

Liu

J

et al..

Chin J Plastic Reconstruc Surg

.

2021

;

3

:

95

–

102

.

[10.1016/S2096-6911(21)00090-X](https://doi.org/10.1016/S2096-6911\(21\)00090-X)

.

Jo

C

,

Zhang

J

,

Tam

JM

et al..

Mater Tod Bio

.

2023

;

19

:

100560

.

[10.1016/J.MTBIO.2023.100560](https://doi.org/10.1016/J.MTBIO.2023.100560)

.

Johnson

D

,

Gilbert

L

..

New Phytol

.

2015

;

205

:

1448

–

53

.

[10.1111/NPH.13115](https://doi.org/10.1111/NPH.13115)

.

Jones

RM

,

Reynolds

RW

,

Thurston

AK

et al..

IEEE J Electromagnet RF Microwaves Med Biol

.

2024

;

1

–

8

.

[10.1109/JERM.2024.3476444](https://doi.org/10.1109/JERM.2024.3476444)

.

Karst

J

,

Jones

MD

,

Hoeksema

JD

..

Nat Ecol Evol

.

2023

;

7

:

501

–

11

.

[10.1038/s41559-023-01986-1](https://doi.org/10.1038/s41559-023-01986-1)

.

Keener

J

,

Sneyd

J

.. In

Keener

J

,

Sneyd

J

(eds),

Mathematical Physiology: I: Cellular Physiology

.

New York, NY

:

Springer

,

2009

,

347

–

84

.

[10.1007/978-0-387-75847-3\_8](https://doi.org/10.1007/978-0-387-75847-3_8)

.

Ketchum

KA

,

Joiner

WJ

,

Sellers

AJ

et al..

Nature

.

1995

;

376

:

690

–

5

.

[10.1038/376690a0](https://doi.org/10.1038/376690a0)

.

Kim

HS

,

Kim

JE

,

Hwangbo

A

et al..

Fungal Genet Biol

.

2021

;

149

:

103540

.

[10.1016/J.FGB.2021.103540](https://doi.org/10.1016/J.FGB.2021.103540)

.

Koo Lee

YE

,

Kopelman

R

..

Methods Enzymol

.

2012

;

504

:

419

–

70

.

[10.1016/B978-0-12-391857-4.00021-5](https://doi.org/10.1016/B978-0-12-391857-4.00021-5)

.

Kropf

DL

,

Caldwell

JH

,

Gow

NAR

et al..

J Cell Biol

.

1984

;

99

:

486

–

96

.

[10.1083/JCB.99.2.486](https://doi.org/10.1083/JCB.99.2.486)

.

Kropf

DL

..

J Cell Biol

.

1986

;

102

:

1209

–

16

.

[10.1083/jcb.102.4.1209%J](https://doi.org/10.1083/jcb.102.4.1209%J)

.

Kulkarni

RU

,

Miller

EW

..

Biochemistry

.

2017

;

56

:

5171

–

7

.

Kulkarni

S

,

Nene

S

,

Joshi

K

..

Process Biochem

.

2017

;

61

:

1

–

11

.

[10.1016/j.procbio.2017.06.012](https://doi.org/10.1016/j.procbio.2017.06.012)

.

Lee

J

,

Calvo

P

..

Synthese

.

2023

;

202

:

1

–

30

.

[10.1007/S11229-023-04398-7/METRICS](https://doi.org/10.1007/S11229-023-04398-7/METRICS)

.

Lesage

F

,

Guillemare

E

,

Fink

M

et al..

J Biol Chem

.

1996

;

271

:

4183

–

7

.

[10.1074/jbc.271.8.4183](https://doi.org/10.1074/jbc.271.8.4183)

.

Lever

MC

,

Robertson

BEM

,

Buchan

ADB

et al..

Mycol Res

.

1994

;

98

:

301

–

6

.

[10.1016/S0953-7562(09)80458-9](https://doi.org/10.1016/S0953-7562\(09\)80458-9)

.

Levin

M

,

Pezzulo

G

,

Finkelstein

JM

..

Annu Rev Biomed Eng

.

2017

;

19

:

353

–

87

.

[10.1146/annurev-bioeng-071114-040647](https://doi.org/10.1146/annurev-bioeng-071114-040647)

.

Levina

NN

,

Dunina-Barkovskaya

AY

,

Shabala

S

et al..

J Membr Biol

.

2002

;

188

:

213

–

26

.

[10.1007/s00232-001-0185-z](https://doi.org/10.1007/s00232-001-0185-z)

.

Li

K

,

Jia

J

,

Wu

N

et al..

Front Bioeng Biotechnol

.

2022

;

10

:

1067869

.

[10.3389/FBIOE.2022.1067869/BIBTEX](https://doi.org/10.3389/FBIOE.2022.1067869/BIBTEX)

.

Linder

MB

,

Szilvay

GR

,

Nakari-Setälä

T

et al..

FEMS Microbiol Rev

.

2005

;

29

:

877

–

96

.

[10.1016/J.FEMSRE.2005.01.004](https://doi.org/10.1016/J.FEMSRE.2005.01.004)

.

Loukin

SH

,

Vaillant

B

,

Zhou

XL

et al..

EMBO J

.

1997

;

16

:

4817

–

25

.

[10.1093/EMBOJ/16.16.4817](https://doi.org/10.1093/EMBOJ/16.16.4817)

.

Luciano-Rosario

D

,

Eagan

JL

,

Aryal

N

et al..

mBio

.

2022

;

13

.

[10.1128/MBIO.02754-22/SUPPL\_FILE/MBIO.02754-22-S0007.TIF](https://doi.org/10.1128/MBIO.02754-22/SUPPL_FILE/MBIO.02754-22-S0007.TIF)

.

Martinac

B

,

Saimi

Y

,

Kung

C

..

Physiol Rev

.

2008

;

88

:

1449

.

[10.1152/PHYSREV.00005.2008](https://doi.org/10.1152/PHYSREV.00005.2008)

.

Mayne

R

,

Roberts

N

,

Phillips

N

et al..

Biosystems

.

2023

;

229

:

104933

.

[10.1016/J.BIOSYSTEMS.2023.104933](https://doi.org/10.1016/J.BIOSYSTEMS.2023.104933)

.

McGillivray

AM

,

Gow

NAR

..

J Gen Microbiol

.

1986

;

132

:

2515

–

25

.

[10.1099/00221287-132-9-2515/CITE/REFWORKS](https://doi.org/10.1099/00221287-132-9-2515/CITE/REFWORKS)

.

McLaughlin

KA

,

Levin

M

..

Dev Biol

.

2018

;

433

:

177

–

89

.

Meyer

V

,

Andersen

MR

,

Brakhage

AA

et al..

Fungal Biol Biotechnol

.

2016

;

3

:

1

–

17

.

[10.1186/S40694-016-0024-8/TABLES/3](https://doi.org/10.1186/S40694-016-0024-8/TABLES/3)

.

Meyer

V

..

Fungal Biol Biotechnol

.

2022

;

9

:

1

–

4

.

[10.1186/S40694-022-00137-8/FIGURES/1](https://doi.org/10.1186/S40694-022-00137-8/FIGURES/1)

.

Moratto

E

,

Rothery

S

,

Bozkurt

TO

et al..

Phys Biol

.

2023

;

20

:

056005

.

[10.1088/1478-3975/ACE751](https://doi.org/10.1088/1478-3975/ACE751)

.

Moratto

E

,

Sena

G

..

Bioelectricity

.

2023

;

5

:

47

–

54

.

[10.1089/BIOE.2023.0001](https://doi.org/10.1089/BIOE.2023.0001)

.

Moratto

E

,

Tang

Z

,

Bozkurt

TO

et al..

Sci Rep

.

2024

;

14

:

1

–

10

.

[10.1038/s41598-024-68730-y](https://doi.org/10.1038/s41598-024-68730-y)

.

Morell

P

,

Quarles

RH

.. In:

Basic Neurochemistry: Molecular, Cellular and Medical Aspects

. Vol.

6

.

New York, NY

:

Raven Press

,

1999

.

Morris

BM

,

Gow

NAR

..

Physiol Biochem

.

1993

;

83

:

877

.

Mousavi

SAR

,

Chauvin

A

,

Pascaud

F

et al..

Nature

.

2013

;

500

:

422

–

6

.

[10.1038/NATURE12478](https://doi.org/10.1038/NATURE12478)

.

Navarro-González

M

,

Arndt

M

,

Zomorrodi

M

et al.. In:

Proceedings of the Seventh International Conference on Mushroom Biology and Mushroom Products (ICMBMP7) 2011

. Vol.

1

.

Bordeaux

:

INRA Bordeaux

,

2011

,

175

–

87

.

Neher

E

,

Sakmann

B

..

Sci Am

.

1992

;

266

:

44

–

51

.

[10.1038/scientificamerican0392-44](https://doi.org/10.1038/scientificamerican0392-44)

.

Nuccitelli

R

..

Curr Top Dev Biol

.

2003

;

58

:

1

–

26

.

Nuccitelli

R

..

Modern Cell Biol

.

1990

;

9

:

273

–

310

.

Olsson

S

,

Gray

SN

..

FEMS Microbiol Ecol

.

1998

;

26

:

109

–

20

.

[10.1016/S0168-6496(98)00026-9](https://doi.org/10.1016/S0168-6496\(98\)00026-9)

.

Olsson

S

,

Hansson

BS

..

Naturwissenschaften

.

1995

;

82

:

30

–

31

.

[10.1007/bf01167867](https://doi.org/10.1007/bf01167867)

.

Olsson

S

,

Jennings

DH

..

Exp Mycol

.

1991a

;

15

:

292

–

301

.

[10.1016/0147-5975(91)90032-9](https://doi.org/10.1016/0147-5975\(91\)90032-9)

.

Olsson

S

,

Jennings

DH

..

Exp Mycol

.

1991b

;

15

:

302

–

9

.

[10.1016/0147-5975(91)90033-A](https://doi.org/10.1016/0147-5975\(91\)90033-A)

.

Olsson

S

.. In:

Biology of the Fungal Cell

.

Berlin

:

Springer

,

2001

,

125

–

41

.

[10.1007/978-3-662-06101-5\_6](https://doi.org/10.1007/978-3-662-06101-5_6)

.

Oyarte Galvez

L

,

Bisot

C

,

Bourrianne

P

et al..

Nature

.

2025

;

639

:

172

–

80

.

[10.1038/s41586-025-08614-x](https://doi.org/10.1038/s41586-025-08614-x)

.

Pajić

T

,

Stevanović

K

,

Todorović

NV

et al..

Microsyst Nanoeng

.

2024

;

10

:

1

–

17

.

[10.1038/s41378-024-00664-x](https://doi.org/10.1038/s41378-024-00664-x)

.

Petsev

D

.

Emulsions: Structure, Stability and Interactions

.

Amsterdam

:

Elsevier

,

2004

.

ISBN: 9780080472652

.

Potapova

T

.. In:

Witzany

G

(ed.),

Biocommunication of Fungi

.

Dordrecht

:

Springer

,

2012

,

103

–

14

.

[10.1007/978-94-007-4264-2\_7---LB—Potapova2012](https://doi.org/10.1007/978-94-007-4264-2_7---LB%E2%80%94Potapova2012)

.

Potapova

TV

,

Levina

NN

,

Belozerskaya

TA

et al..

Arch Microbiol

.

1984

;

137

:

262

–

5

.

[10.1007/BF00414555/METRICS](https://doi.org/10.1007/BF00414555/METRICS)

.

Prindle

A

,

Liu

J

,

Asally

M

et al..

Nature

.

2015

;

527

:

59

.

[10.1038/nature15709](https://doi.org/10.1038/nature15709)

[https://www.nature.com/articles/nature15709#supplementary-information](https://www.nature.com/articles/nature15709#supplementary-information)

.

Prole

DL

,

Taylor

CW

..

PLoS One

.

2012

;

7

:

e42404

.

[10.1371/JOURNAL.PONE.0042404](https://doi.org/10.1371/JOURNAL.PONE.0042404)

.

Rayner

ADM

,

Griffith

GS

,

Ainsworth

AM

.. In:

The Growing Fungus

.

Berlin

:

Springer

,

1995

,

21

–

40

.

Richter

F

,

Bindschedler

S

,

Calonne-Salmon

M

et al..

FEMS Microbiol Rev

.

2022

;

46

.

[10.1093/FEMSRE/FUAC039](https://doi.org/10.1093/FEMSRE/FUAC039)

.

Rickerts

V

.. In:

Bundesgesundheitsblatt—Gesundheitsforschung—Gesundheitsschutz

. Vol.

62

.

Berlin

:

Springer

,

2019

,

646

–

51

.

[10.1007/s00103-019-02931-z](https://doi.org/10.1007/s00103-019-02931-z)

.

Roberts

SK

,

Dixon

GK

,

Dunbar

SJ

et al..

New Phytol

.

1997

;

137

:

579

–

85

.

[10.1046/j.1469-8137.1997.00862.x](https://doi.org/10.1046/j.1469-8137.1997.00862.x)

.

Roper

M

,

Seminara

A

..

Annu Rev Fluid Mech

.

2019

;

51

:

511

–

38

.

[10.1146/annurev-fluid-122316045308](https://doi.org/10.1146/annurev-fluid-122316045308)

.

Schmieder

SS

,

Stanley

CE

,

Rzepiela

A

et al..

Curr Biol

.

2019

;

29

:

217

–

28.e4

.

[10.1016/J.CUB.2018.11.058](https://doi.org/10.1016/J.CUB.2018.11.058)

.

Schyck

S

,

Marchese

P

,

Amani

M

et al..

Global Challenges

.

2024

;

8

:

2400104

.

[10.1002/GCH2.202400104](https://doi.org/10.1002/GCH2.202400104)

.

Sibaoka

T

..

Symp Soc Exp Biol

.

1966

;

20

:

49

–

73

.

Simard

SW

,

Durall

DM

..

Can J Bot

.

2011

;

82

:

1140

–

65

.

[10.1139/B04-116](https://doi.org/10.1139/B04-116)

.

Slayman

CL

,

Scott Long

W

,

Gradmann

D

..

Biochim Biophys Acta Biomembr

.

1976

;

426

:

732

–

44

.

[10.1016/0005-2736(76)90138-3](https://doi.org/10.1016/0005-2736\(76\)90138-3)

.

Stanley

CE

,

Grossmann

G

,

Casadevall i Solvas

X

et al..

Lab Chip

.

2016

;

16

:

228

–

41

.

[10.1039/C5LC01285F](https://doi.org/10.1039/C5LC01285F)

.

Steinberg

G

,

Harmer

NJ

,

Schuster

M

et al..

Fungal Genet Biol

.

2017

;

109

:

53

–

55

.

[10.1016/J.FGB.2017.10.006](https://doi.org/10.1016/J.FGB.2017.10.006)

.

Stephenson

KS

,

Gow

NAR

,

Davidson

FA

et al..

Fungal Biol

.

2014

;

118

:

287

–

94

.

[10.1016/j.funbio.2013.12.007](https://doi.org/10.1016/j.funbio.2013.12.007)

.

Stump

RF

,

Robinson

KR

,

Harold

RL

et al..

Proc Natl Acad Sci

.

1980

;

77

:

6673

–

7

.

Swafford

AJM

,

Oakley

TH

..

J Exp Biol

.

2018

;

221

:

jeb163196

.

[10.1242/jeb.163196](https://doi.org/10.1242/jeb.163196)

.

Szechyńska-Hebda

M

,

Lewandowska

M

,

Karpiński

S

.. In:

Frontiers in Physiology

. Vol.

8

,

Lausanne

:

Frontiers Media S.A

,

2017

,

684

.

[10.3389/fphys.2017.00684](https://doi.org/10.3389/fphys.2017.00684)

.

Takeo Kamada

B

..

J Exp Biol

.

1934

;

11

:

94

–

102

.

[10.1242/JEB.11.1.94](https://doi.org/10.1242/JEB.11.1.94)

.

The Lancet Infectious Diseases

..

Lancet Infect Dis

.

2023

;

23

:

763

.

[10.1016/S1473-3099(23)00380-8](https://doi.org/10.1016/S1473-3099\(23\)00380-8)

.

Thomas

MA

,

Cooper

RL

..

Plant Signal Behav

.

2022

;

17

.

[10.1080/15592324.2022.2129291](https://doi.org/10.1080/15592324.2022.2129291)

.

Tjallingii

WF

..

Entomol Exp Appl

.

1985

;

38

:

177

–

86

.

Townsend

BB

..

Trans Br Mycol Soc

.

1954

;

37

:

222

–

33

.

[10.1016/S0007-1536(54)80004-0](https://doi.org/10.1016/S0007-1536\(54\)80004-0)

.

van der Klei

IJ

,

Veenhuis

M

..

Biochim Biophys Acta Mol Cell Res

.

2006

;

1763

:

1364

–

73

.

[10.1016/J.BBAMCR.2006.09.014](https://doi.org/10.1016/J.BBAMCR.2006.09.014)

.

Vodeneev

V

,

Akinchits

E

,

Sukhov

V

..

Plant Signal Behav

.

2015

;

10

:

e1057365

.

[10.1080/15592324.2015.1057365](https://doi.org/10.1080/15592324.2015.1057365)

.

Wood

J

,

Tordoff

GM

,

Jones

TH

et al..

Mycol Res

.

2006

;

110

:

985

–

93

.

[10.1016/J.MYCRES.2006.05.013](https://doi.org/10.1016/J.MYCRES.2006.05.013)

.

Wösten

HAB

,

de Vocht

ML

..

Biochim Biophys Acta Rev Biomembr

.

2000

;

1469

:

79

–

86

.

[10.1016/S0304-4157(00)00002-2](https://doi.org/10.1016/S0304-4157\(00\)00002-2)

.

Yang

HH

,

St-Pierre

F

..

J Neurosci

.

2016

;

36

:

9977

–

89

.

[10.1523/JNEUROSCI.1095-16.2016](https://doi.org/10.1523/JNEUROSCI.1095-16.2016)

.

Youatt

J

,

Gow

NAR

,

Gooday

GW

..

Protoplasma

.

1988

;

146

:

118

–

26

.

[10.1007/BF01405920/METRICS](https://doi.org/10.1007/BF01405920/METRICS)

.

Zhao

C

,

Tombola

F

..

Commun Biol

.

2021

;

4

:

1

–

13

.

[10.1038/s42003-021-01792-0](https://doi.org/10.1038/s42003-021-01792-0)

.

Zhao

Y

,

Inayat

S

,

Dikin

DA

et al..

Proc Inst Mech Eng Part N J Nanoeng Nanosyst

.

2008

;

222

:

1

–

11

.

[10.1243/17403499jnn149](https://doi.org/10.1243/17403499jnn149)

.

Zhou

XL

,

Stumpf

MA

,

Hoch

HC

et al..

Science

.

1991

;

253

:

1415

–

7

.

[10.1126/science.1716786](https://doi.org/10.1126/science.1716786)

.

Zhou

XL

,

Vaillant

B

,

Loukin

SH

et al..

FEBS Lett

.

1995

;

373

:

170

–

6

.

[10.1016/0014-5793(95)01035-D](https://doi.org/10.1016/0014-5793\(95\)01035-D)

.

Zimmermann

MR

,

Maischak

H

,

Mithöfer

A

et al..

Plant Physiol

.

2009

;

149

:

1593

–

600

.

[10.1104/pp.108.133884](https://doi.org/10.1104/pp.108.133884)

.

## Supplementary data

[fuaf009\_Supplemental\_File](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/femsre/49/10.1093_femsre_fuaf009/1/fuaf009_supplemental_file.docx?Expires=1781219807&Signature=Xp1wiEBfUaBeOZVEJU7srn-~GKXCXKWTRXtV4KkG7ayA3jV-ADJswRfxjgThydYigW~wR7jbvacPVN0HH3mCwSsC~ZP6TfC9dkfHLWBQMnrKnJYLqy9T~0eRGPnDOVjvZyknI80ybJ2NCkQf3WiPFym67wJQ0G3xlI3Nw6c2GxBrTBAJUkbI0V8rMs41ZUaKWMmV0tmndVc1mbUiT8JNXVGXyTYZZXeBBXeXaE3WwzuDYJgW4xlca9FcDk3fvta0RDL~ud3~Y2f9HMjphoFgb0lIMcQUchXgN~xDV5GZlggVxY5v4nlmGlKQ4oMudTjb5XVxDJe2UE3gn~Hfh2B2Ng__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) - docx file