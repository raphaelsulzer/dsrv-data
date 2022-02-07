# Deep Surface Reconstruction from Point Clouds with Visibility Information

[Paper](https://arxiv.org/abs/2202.01810)

Data, code and pretrained models for the paper **Deep Surface Reconstruction from Point Clouds with Visibility Information**.

<table>
<thead>
  <tr align="center">
    <th><img style="width:250px;" src="teaser/sofa_0751_scan.png"></th>
    <th><img style="width:200px; " src="teaser/sofa_0751_co_con.png"></th>
    <th><img style="width:250px;" src="teaser/sofa_0751_scan_aux_los_yellow.png"></th>
    <th><img style="width:200px;" src="teaser/sofa_0751_co_aux.png"></th>
  </tr>
</thead>
<tbody align="center">
  <tr>
    <td>Point cloud</td>
    <td>Reconstruction</td>
    <td>Point cloud with Visibility</td>
    <td>Reconstruction</td>
  </tr>
</tbody>
</table>

## Data

### ModelNet10

- The ModelNet10 models made watertight using [ManifoldPlus](https://github.com/hjwdzh/ManifoldPlus)
can be downloaded [here on Zenodo](https://zenodo.org/record/5920479#.YflZilvMLIE).
- The ModelNet10 scans used in our paper can be downloaded
[here on Zenodo](https://zenodo.org/record/5940164#.YflZolvMLIE). The dataset also includes training and evaluation
data for ConvONet, Points2Surf, Shape As Points, POCO and DGNN.

### ShapeNet*v1* (13 class subset of [Choy et al.](https://arxiv.org/abs/1604.00449))

- The watertight ShapeNet models can be downloaded [here](https://s3.eu-central-1.amazonaws.com/avg-projects/occupancy_networks/data/watertight.zip) (provided by the authors of [ONet](https://arxiv.org/abs/1812.03828)).
- Please open an issue if you are interested in the scans used in our paper.

### Synthetic Rooms Dataset

- The watertight scenes can be downloaded [here](https://s3.eu-central-1.amazonaws.com/avg-projects/convolutional_occupancy_networks/data/room_watertight_mesh.zip) (provided by the authors of [ConvONet](https://arxiv.org/abs/2003.04618)).
- Please open an issue if you are interested in the scans used in our paper.

[//]: # (- The training and evaluation data for ConvONet can be downloaded here.)

[//]: # (- The training data for Shape As Points can be downloaded here.)

### Scanning procedure

If you want to create scans of your own dataset you can use the precompiled `scan` executable. It should work on most Ubuntu systems.

```
scan -w path/to/working_directory -i "" -o output_filename -g mesh_to_scan_filename --export npz
```

For creating the scans used in the paper the follwing settings were used:

```
--points 3000 --noise 0.005 --outliers 0.0
```

## Code

You can find our modified code and pretrained models for the methods tested in the paper below.
All methods support point clouds with and without visibility information.

- [ConvOnet](https://github.com/raphaelsulzer/convolutional_occupancy_networks)
- [Points2Surf](https://github.com/raphaelsulzer/points2surf)
- [Shape As Points](https://github.com/raphaelsulzer/shape_as_points)
- [POCO](https://github.com/raphaelsulzer/POCO)
- [LIG](https://github.com/raphaelsulzer/graphics)
- [DGNN](https://github.com/raphaelsulzer/dgnn)



## References

If you find the code or data in this repository useful, please consider citing the following paper:

```
@misc{sulzer2022deep,
      title={Deep Surface Reconstruction from Point Clouds with Visibility Information}, 
      author={Raphael Sulzer and Loic Landrieu and Alexandre Boulch and Renaud Marlet and Bruno Vallet},
      year={2022},
      eprint={2202.01810},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```





