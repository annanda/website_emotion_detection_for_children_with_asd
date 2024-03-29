# Source Code of Website for the research project "Ethically-driven Multimodal Emotion Detection for Children with Autism"

Source code used for the "Ethically-driven Multimodal Emotion Detection for Children with Autism" project's website.

[Website](http://emotion-asd.datascienceinstitute.ie/)

## Pre-requisites
- Python 3.8 
- Docker

## Installation
### Development
1. Prepare the virtual environment (Create and activate virtual environment with venv).

`python -m venv ./venv`

`source ./venv/bin/activate`

2. Run the script 

`python app.py`

### Deployment with Docker
1. Build the images

`docker compose build`

2. Start the services

`docker compose up -d`


## Licence

This repository is released under dual-licencing:

For non-commercial use of the Software, it is released under
the [3-Cause BSD Licence](https://opensource.org/license/bsd-3-clause/).

For commercial use of the Software, you are required to contact the University of Galway to arrange a commercial
licence.

Please refer to [LICENSE.md](LICENSE.md) file for details on the licence.

### Credits

Photo by Tengyart on Unsplash

Photo by Apaha Spi on Unsplash

Photo by Glenn Carstens-Peters on Unsplash

## Citation

If you use any of the resources provided on this repository in any of your publications we ask you to cite the following
work:

Sousa, Annanda, et al. "**Introducing CALMED: Multimodal Annotated Dataset for Emotion Detection in Children with Autism**."
International Conference on Human-Computer Interaction. Cham: Springer Nature Switzerland, 2023.

----

Author: Annanda Sousa

Author's contact: [annanda.sousa@gmail.com](mailto:annanda.sousa@gmail.com)

----
