main_invalid_request = {
    "detail": [
        {
            "loc": ["query", "member_id"],
            "msg": "field required",
            "type": "value_error.missing",
        },
        {
            "loc": ["query", "strategy"],
            "msg": "field required",
            "type": "value_error.missing",
        },
    ]
}

externals_invalid_request = {
    "detail": [
        {
            "loc": ["query", "member_id"],
            "msg": "field required",
            "type": "value_error.missing",
        }
    ]
}

main_invalid_strategy = {"detail": "Invalid strategy"}

main_integration_mean = {
    "deductible": 1066.6666666666667,
    "oop_max": 5333.333333333333,
    "stop_loss": 11000,
}

main_integration_fmean = {
    "deductible": 1066.6666666666667,
    "stop_loss": 11000.0,
    "oop_max": 5333.333333333333,
}
main_integration_geometric_mean = {
    "deductible": 1062.6585691826112,
    "stop_loss": 10913.928830611068,
    "oop_max": 5313.292845913057,
}
main_integration_harmonic_mean = {
    "deductible": 1058.8235294117646,
    "stop_loss": 10833.333333333332,
    "oop_max": 5294.117647058823,
}
main_integration_median = {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000}
main_integration_median_high = {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000}
main_integration_median_low = {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000}
main_integration_min = {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000}
main_integration_max = {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000}

externals_member_1 = {"deductible": 1200, "oop_max": 6000, "stop_loss": 13000}
externals_member_20 = {"deductible": 1000, "oop_max": 5000, "stop_loss": 10000}
externals_member_2000 = {"deductible": 1200, "oop_max": 6000, "stop_loss": 13000}
