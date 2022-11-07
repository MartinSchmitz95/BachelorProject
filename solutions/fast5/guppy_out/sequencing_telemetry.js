[
    {
        "aggregation": "segment",
        "analysis_id": "b5e18fb5-75e5-462d-94ad-b8c2f6ff0805",
        "basecall_1d": {
            "exit_status_dist": {
                "fail:qscore_filter": 10
            },
            "qscore_dist_temp": [
                {
                    "count": 2,
                    "mean_qscore": 3.0
                },
                {
                    "count": 2,
                    "mean_qscore": 3.5
                },
                {
                    "count": 5,
                    "mean_qscore": 4.0
                },
                {
                    "count": 1,
                    "mean_qscore": 5.0
                }
            ],
            "qscore_sum_temp": {
                "count": 10,
                "mean": 4.05686712265015,
                "sum": 40.5686721801758
            },
            "read_len_events_sum_temp": 66271,
            "seq_len_bases_dist_temp": [
                {
                    "count": 9,
                    "length": 0.0
                },
                {
                    "count": 1,
                    "length": 2000.0
                }
            ],
            "seq_len_bases_sum_temp": 4425,
            "seq_len_events_dist_temp": [
                {
                    "count": 1,
                    "length": 1000.0
                },
                {
                    "count": 3,
                    "length": 2000.0
                },
                {
                    "count": 2,
                    "length": 3000.0
                },
                {
                    "count": 1,
                    "length": 4000.0
                },
                {
                    "count": 1,
                    "length": 14000.0
                },
                {
                    "count": 1,
                    "length": 15000.0
                },
                {
                    "count": 1,
                    "length": 16000.0
                }
            ],
            "speed_bases_per_second_dist_temp": [
                {
                    "count": 1,
                    "speed": 51.0
                },
                {
                    "count": 1,
                    "speed": 53.0
                },
                {
                    "count": 1,
                    "speed": 55.0
                },
                {
                    "count": 1,
                    "speed": 57.0
                },
                {
                    "count": 1,
                    "speed": 63.0
                },
                {
                    "count": 1,
                    "speed": 105.0
                },
                {
                    "count": 1,
                    "speed": 119.0
                },
                {
                    "count": 1,
                    "speed": 125.0
                },
                {
                    "count": 1,
                    "speed": 275.0
                },
                {
                    "count": 1,
                    "speed": 299.0
                }
            ],
            "strand_median_pa": {
                "count": 10,
                "mean": 108.460121154785,
                "sum": 1084.60119628906
            },
            "strand_sd_pa": {
                "count": 10,
                "mean": 4.84605121612549,
                "sum": 48.4605140686035
            }
        },
        "channel_count": 10,
        "context_tags": {
            "experiment_type": "genomic_dna",
            "fast5_output_fastq_in_hdf": "1",
            "fast5_raw": "1",
            "fast5_reads_per_folder": "4000",
            "fastq_enabled": "1",
            "fastq_reads_per_file": "4000",
            "filename": "gxb01103_20180501_fah86018_ga30000_mux_scan_chm13_1_36685",
            "flowcell_type": "flo-min106",
            "kit_classification": "none",
            "local_basecalling": "1",
            "sample_frequency": "4000",
            "sequencing_kit": "sqk-rad004",
            "user_filename_input": "chm13_1"
        },
        "latest_run_time": 62.900749206543,
        "levels_sums": {
            "count": 10,
            "mean": 229.031326293945,
            "open_pore_level_sum": 2290.31323242188
        },
        "opts": {
            "adapter_pt_range_scale": "5.200000",
            "builtin_scripts": "1",
            "calib_detect": "0",
            "calib_max_sequence_length": "3800",
            "calib_min_coverage": "0.600000",
            "calib_min_sequence_length": "3000",
            "calib_reference": "lambda_3.6kb.fasta",
            "chunk_size": "1000",
            "chunks_per_caller": "10000",
            "chunks_per_runner": "1000",
            "cpu_threads_per_caller": "1",
            "device": "",
            "disable_events": "0",
            "disable_pings": "0",
            "dmean_threshold": "1.000000",
            "dmean_win_size": "2",
            "enable_trimming": "1",
            "fast5_out": "1",
            "flowcell": "",
            "gpu_runners_per_device": "2",
            "hp_correct": "1",
            "jump_threshold": "1.000000",
            "kernel_path": "",
            "kit": "",
            "max_search_len": "1000",
            "min_qscore": "7.000000",
            "model_file": "template_r9.4.1_450bps_hac.jsn",
            "num_callers": "2",
            "overlap": "50",
            "override_scaling": "0",
            "ping_segment_duration": "60",
            "ping_url": "https://ping.oxfordnanoportal.com/basecall",
            "port": "",
            "print_workflows": "0",
            "pt_median_offset": "2.500000",
            "pt_minimum_read_start_index": "30",
            "pt_required_adapter_drop": "30.000000",
            "pt_scaling": "0",
            "qscore_filtering": "0",
            "qscore_offset": "0.250000",
            "qscore_scale": "0.910000",
            "quiet": "0",
            "read_id_list": "",
            "records_per_fastq": "4000",
            "recursive": "0",
            "reverse_sequence": "0",
            "scaling_mad": "0.000000",
            "scaling_med": "0.000000",
            "stay_penalty": "1.000000",
            "temp_bias": "1.000000",
            "temp_weight": "1.000000",
            "trace_categories_logs": "",
            "trim_min_events": "3",
            "trim_strategy": "dna",
            "trim_threshold": "2.500000",
            "u_substitution": "0",
            "verbose_logs": "0"
        },
        "read_count": 10,
        "reads_per_channel_dist": [
            {
                "channel": 209,
                "count": 1
            },
            {
                "channel": 216,
                "count": 1
            },
            {
                "channel": 234,
                "count": 1
            },
            {
                "channel": 252,
                "count": 1
            },
            {
                "channel": 258,
                "count": 1
            },
            {
                "channel": 313,
                "count": 1
            },
            {
                "channel": 366,
                "count": 1
            },
            {
                "channel": 422,
                "count": 1
            },
            {
                "channel": 474,
                "count": 1
            },
            {
                "channel": 502,
                "count": 1
            }
        ],
        "run_id": "c755b15f8f55d8df50b420a6932c41e787fb781f",
        "segment_duration": 60,
        "segment_number": 1,
        "segment_type": "guppy-acquisition",
        "software": {
            "analysis": "1d_basecalling",
            "name": "guppy-basecalling",
            "version": "3.0.3+7e7b7d0"
        },
        "tracking_id": {
            "asic_id": "19807616",
            "asic_id_eeprom": "2553690",
            "asic_temp": "35.471043",
            "auto_update": "0",
            "auto_update_source": "https://mirror.oxfordnanoportal.com/software/MinKNOW/",
            "bream_is_standard": "1",
            "device_id": "GA30000",
            "device_type": "gridion",
            "exp_script_name": "bb52230716971370395e07ff0e24c8cc07f8ecb1-caaac7b6c675349ae28ee47384e3a2c96f870fe4",
            "exp_script_purpose": "mux_scan",
            "exp_start_time": "2018-05-01T16:07:15Z",
            "flow_cell_id": "FAH86018",
            "heatsink_temp": "34.769531",
            "hostname": "GXB01103",
            "installation_type": "nc",
            "local_firmware_file": "1",
            "msg_id": "88516f22-8bfc-43a4-af6d-66db20deb2fa",
            "operating_system": "ubuntu 16.04",
            "protocol_run_id": "37cf86aa-1c85-4d29-bb5d-4afae567e16a",
            "protocols_version": "1.11.3.1",
            "run_id": "c755b15f8f55d8df50b420a6932c41e787fb781f",
            "sample_id": "CHM13_1",
            "time_stamp": "2022-11-03T15:51:17Z",
            "usb_config": "firm_1.2.3_ware#rbt_4.5.6_rbt#ctrl#USB3",
            "version": "1.11.8"
        }
    },
    {
        "aggregation": "cumulative",
        "analysis_id": "b5e18fb5-75e5-462d-94ad-b8c2f6ff0805",
        "basecall_1d": {
            "exit_status_dist": {
                "fail:qscore_filter": 10
            },
            "qscore_dist_temp": [
                {
                    "count": 2,
                    "mean_qscore": 3.0
                },
                {
                    "count": 2,
                    "mean_qscore": 3.5
                },
                {
                    "count": 5,
                    "mean_qscore": 4.0
                },
                {
                    "count": 1,
                    "mean_qscore": 5.0
                }
            ],
            "qscore_sum_temp": {
                "count": 10,
                "mean": 4.05686712265015,
                "sum": 40.5686721801758
            },
            "read_len_events_sum_temp": 66271,
            "seq_len_bases_dist_temp": [
                {
                    "count": 9,
                    "length": 0.0
                },
                {
                    "count": 1,
                    "length": 2000.0
                }
            ],
            "seq_len_bases_sum_temp": 4425,
            "seq_len_events_dist_temp": [
                {
                    "count": 1,
                    "length": 1000.0
                },
                {
                    "count": 3,
                    "length": 2000.0
                },
                {
                    "count": 2,
                    "length": 3000.0
                },
                {
                    "count": 1,
                    "length": 4000.0
                },
                {
                    "count": 1,
                    "length": 14000.0
                },
                {
                    "count": 1,
                    "length": 15000.0
                },
                {
                    "count": 1,
                    "length": 16000.0
                }
            ],
            "speed_bases_per_second_dist_temp": [
                {
                    "count": 1,
                    "speed": 51.0
                },
                {
                    "count": 1,
                    "speed": 53.0
                },
                {
                    "count": 1,
                    "speed": 55.0
                },
                {
                    "count": 1,
                    "speed": 57.0
                },
                {
                    "count": 1,
                    "speed": 63.0
                },
                {
                    "count": 1,
                    "speed": 105.0
                },
                {
                    "count": 1,
                    "speed": 119.0
                },
                {
                    "count": 1,
                    "speed": 125.0
                },
                {
                    "count": 1,
                    "speed": 275.0
                },
                {
                    "count": 1,
                    "speed": 299.0
                }
            ],
            "strand_median_pa": {
                "count": 10,
                "mean": 108.460121154785,
                "sum": 1084.60119628906
            },
            "strand_sd_pa": {
                "count": 10,
                "mean": 4.84605121612549,
                "sum": 48.4605140686035
            }
        },
        "channel_count": 10,
        "context_tags": {
            "experiment_type": "genomic_dna",
            "fast5_output_fastq_in_hdf": "1",
            "fast5_raw": "1",
            "fast5_reads_per_folder": "4000",
            "fastq_enabled": "1",
            "fastq_reads_per_file": "4000",
            "filename": "gxb01103_20180501_fah86018_ga30000_mux_scan_chm13_1_36685",
            "flowcell_type": "flo-min106",
            "kit_classification": "none",
            "local_basecalling": "1",
            "sample_frequency": "4000",
            "sequencing_kit": "sqk-rad004",
            "user_filename_input": "chm13_1"
        },
        "latest_run_time": 62.900749206543,
        "levels_sums": {
            "count": 10,
            "mean": 229.031326293945,
            "open_pore_level_sum": 2290.31323242188
        },
        "opts": {
            "adapter_pt_range_scale": "5.200000",
            "builtin_scripts": "1",
            "calib_detect": "0",
            "calib_max_sequence_length": "3800",
            "calib_min_coverage": "0.600000",
            "calib_min_sequence_length": "3000",
            "calib_reference": "lambda_3.6kb.fasta",
            "chunk_size": "1000",
            "chunks_per_caller": "10000",
            "chunks_per_runner": "1000",
            "cpu_threads_per_caller": "1",
            "device": "",
            "disable_events": "0",
            "disable_pings": "0",
            "dmean_threshold": "1.000000",
            "dmean_win_size": "2",
            "enable_trimming": "1",
            "fast5_out": "1",
            "flowcell": "",
            "gpu_runners_per_device": "2",
            "hp_correct": "1",
            "jump_threshold": "1.000000",
            "kernel_path": "",
            "kit": "",
            "max_search_len": "1000",
            "min_qscore": "7.000000",
            "model_file": "template_r9.4.1_450bps_hac.jsn",
            "num_callers": "2",
            "overlap": "50",
            "override_scaling": "0",
            "ping_segment_duration": "60",
            "ping_url": "https://ping.oxfordnanoportal.com/basecall",
            "port": "",
            "print_workflows": "0",
            "pt_median_offset": "2.500000",
            "pt_minimum_read_start_index": "30",
            "pt_required_adapter_drop": "30.000000",
            "pt_scaling": "0",
            "qscore_filtering": "0",
            "qscore_offset": "0.250000",
            "qscore_scale": "0.910000",
            "quiet": "0",
            "read_id_list": "",
            "records_per_fastq": "4000",
            "recursive": "0",
            "reverse_sequence": "0",
            "scaling_mad": "0.000000",
            "scaling_med": "0.000000",
            "stay_penalty": "1.000000",
            "temp_bias": "1.000000",
            "temp_weight": "1.000000",
            "trace_categories_logs": "",
            "trim_min_events": "3",
            "trim_strategy": "dna",
            "trim_threshold": "2.500000",
            "u_substitution": "0",
            "verbose_logs": "0"
        },
        "read_count": 10,
        "reads_per_channel_dist": [
            {
                "channel": 209,
                "count": 1
            },
            {
                "channel": 216,
                "count": 1
            },
            {
                "channel": 234,
                "count": 1
            },
            {
                "channel": 252,
                "count": 1
            },
            {
                "channel": 258,
                "count": 1
            },
            {
                "channel": 313,
                "count": 1
            },
            {
                "channel": 366,
                "count": 1
            },
            {
                "channel": 422,
                "count": 1
            },
            {
                "channel": 474,
                "count": 1
            },
            {
                "channel": 502,
                "count": 1
            }
        ],
        "run_id": "c755b15f8f55d8df50b420a6932c41e787fb781f",
        "segment_duration": 60,
        "segment_number": 1,
        "segment_type": "guppy-acquisition",
        "software": {
            "analysis": "1d_basecalling",
            "name": "guppy-basecalling",
            "version": "3.0.3+7e7b7d0"
        },
        "tracking_id": {
            "asic_id": "19807616",
            "asic_id_eeprom": "2553690",
            "asic_temp": "35.471043",
            "auto_update": "0",
            "auto_update_source": "https://mirror.oxfordnanoportal.com/software/MinKNOW/",
            "bream_is_standard": "1",
            "device_id": "GA30000",
            "device_type": "gridion",
            "exp_script_name": "bb52230716971370395e07ff0e24c8cc07f8ecb1-caaac7b6c675349ae28ee47384e3a2c96f870fe4",
            "exp_script_purpose": "mux_scan",
            "exp_start_time": "2018-05-01T16:07:15Z",
            "flow_cell_id": "FAH86018",
            "heatsink_temp": "34.769531",
            "hostname": "GXB01103",
            "installation_type": "nc",
            "local_firmware_file": "1",
            "msg_id": "3dc658ce-91ee-4f69-8fa7-5132a85353a3",
            "operating_system": "ubuntu 16.04",
            "protocol_run_id": "37cf86aa-1c85-4d29-bb5d-4afae567e16a",
            "protocols_version": "1.11.3.1",
            "run_id": "c755b15f8f55d8df50b420a6932c41e787fb781f",
            "sample_id": "CHM13_1",
            "time_stamp": "2022-11-03T15:51:17Z",
            "usb_config": "firm_1.2.3_ware#rbt_4.5.6_rbt#ctrl#USB3",
            "version": "1.11.8"
        }
    }
]