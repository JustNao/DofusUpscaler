<div align="center">
<h3 align="center">Dofus Upscaler</h3>

  <p align="center">
    Upscaler pour les items et cartes de dofus 2.XX (testé sur Dofus > 2.67)
  </p>
</div>

## Principe

Les sprites dédiées aux items et cartes du jeu sont stockées dans des d2p. Dofus Upscaler extrait ces images, les écrase par des versions upscale x4 (obtenus grâce à la suite Topaz), puis les repack en un d2p modifié. Le jeu charge alors les images modifiées, et les affiche à la place des images de base.
La modification est valable jusqu'à la prochaine mise à jour du jeu, (par le checksum du launcher), qui écrasera le d2p modifié par un d2p de base. Il faudra alors relancer Dofus Upscaler pour réappliquer les modifications.

> **Note**
> Plus la résolution de votre écran est élevée, plus vous allez noter la différence. A 1080p c'est pas ouf.

## Exemples

<div align="center">
  <h3>Item original</h3>

[![imagex1.png](https://i.postimg.cc/DzJjtbfh/imagex1.png)](https://postimg.cc/bGP9nr2V)

</div>
<div align="center">
  <h3>Item upscale</h3>

[![imagex2.png](https://i.postimg.cc/ryJJZ9GW/imagex2.png)](https://postimg.cc/4nYVmVSN)

</div>
<div align="center">
  <h3>Carte originale</h3>

[![cartex1.png](https://i.postimg.cc/6pdTzMnx/cartex1.png)](https://postimg.cc/LJ8H8Bxx)

</div><div align="center">
  <h3>Carte upscale</h3>

[![cartex2.png](https://i.postimg.cc/qR7RJ0Yp/cartex2.png)](https://postimg.cc/mc0RVxBn)

</div>

## Copyright

Merci beaucoup à balciseri pour son [PyDofus](https://github.com/balciseri/PyDofus) qui permet de facilement pack/unpack des d2p.
