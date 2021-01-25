def time_loader():
    return "30"


def get_start_time():
    return "20h42"


def get_season(user=None):
    if user is None:
        return ["The Conjugal Configuration",
                "The Wedding Gift Wormhole",
                "The Procreation Calculation",
                "The Tam Turbulence",
                "The Planetarium Collision",
                "The Imitation Perturbation",
                "The Grant Allocation Derivation",
                "The Consummation Deviation",
                "The Citation Negation",
                "The VCR Illumination",
                "The Paintball Scattering",
                "The Propagation Proposition",
                "The Confirmation Polarization",
                "The Meteorite Manifestation",
                "The Donation Oscillation",
                "The D & D Vortex",
                "The Conference Valuation",
                "The Laureate Accumulation",
                "The Inspiration Deprivation",
                "The Decision Reverberation",
                "The Plagiarism Schism",
                "The Maternal Conclusion",
                "The Change Constant",
                "The Stockholm Syndrome"]

    else:
        return [['The Conjugal Configuration', True],
                ['The Wedding Gift Wormhole', True],
                ['The Procreation Calculation', True],
                ['The Tam Turbulence', True],
                ['The Planetarium Collision', True],
                ['The Imitation Perturbation', True],
                ['The Grant Allocation Derivation', True],
                ['The Consummation Deviation', True],
                ['The Citation Negation', True],
                ['The VCR Illumination', False],
                ['The Paintball Scattering', False],
                ['The Propagation Proposition', False],
                ['The Confirmation Polarization', False],
                ['The Meteorite Manifestation', False],
                ['The Donation Oscillation', False],
                ['The D & D Vortex', False],
                ['The Conference Valuation', False],
                ['The Laureate Accumulation', False],
                ['The Inspiration Deprivation', False],
                ['The Decision Reverberation', False],
                ['The Plagiarism Schism', False],
                ['The Maternal Conclusion', False],
                ['The Change Constant', False],
                ['The Stockholm Syndrome', False]]


def get_movies():
    return [["The Philosopher's Stone", 152, True],
            ["The Chamber of Secrets", 161, True],
            ["The Prisoner of Azkaban", 142, False],
            ["the Goblet of Fire", 157, True],
            ["the Order of the Phoenix", 138, False],
            ["the Half-Blood Prince", 153, True],
            ["the Deathly Hallows – Part 1", 126, False],
            ["the Deathly Hallows – Part 2", 130, False]]
