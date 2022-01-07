# Changelog
All notable changes to this project will be documented in this file.

The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to
[Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security



## [5.0.2] - 2022-01-07

### Changed
- Library `minted`: Temporary patch `\tcbTemporaryPatchMintedFancyvrb` removed
    because of update for package `minted` (2021/12/24). This is now the required
    version for `tcolorbox` (issue #158)

### Fixed
- Using the `documentation` library with `minted` was broken
- Library `theorems`: New implementation had title expansion with problems (issue #165)




## [5.0.1] - 2021-12-20

### Fixed
- Library `minted`: Patch `\tcbTemporaryPatchMintedFancyvrb` fixed (issue #158)
- Fix for issue #157 disabled unbreakability for hbox type boxes (issue #162)
    This also affected boxes with sidebyside content


## [5.0.0] - 2021-12-16

### Added
- Library `skins`: Option `attach boxed title to top text left`
- Library `skins`: Option `attach boxed title to top text right`
- Library `skins`: Option `attach boxed title to bottom text left`
- Library `skins`: Option `attach boxed title to bottom text right`
- Library `theorems`: Option `theorem number`
- Library `minted`: Option `default minted options`
- Library `minted`: Temporary patch `\tcbTemporaryPatchMintedFancyvrb`
    for the current minted/fancyvrb package clash (issue #158)

### Changed
- Changelog is switched to Markdown for entries from 2021 on
  [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
- From now on version numbers adhere to
  [Semantic Versioning](http://semver.org/spec/v2.0.0.html)
- Library `documentation`: warn about not installed `marvosym` and `pifont` (issue #153)
- Environments wrapped with `\tcolorboxenvironment` are now compatible with 
  all three capture modes `minipage`, `hbox`, and `fitbox` (issue #154)
- Meaningful error prompts when using unknown capture modes (issue #156)
- Library `raster`: Inside a raster, `tcbrasternum` can now be 
    referenced using `label={mylabel}`, if the box is not numbered otherwise (issue #81 and #119)
- Library `theorem`: Theorems with empty display name are now possible without glitches
- Library `theorem`: Major code parts rewritten in expl3 code
- Internal layer accounting changed from LaTeX to TeX code to avoid problems with counter macro
    manipulations by amsmath alignment environments (issue #160)
- Library `minted`: Option `minted options` now initialized with `default minted options`
- Library `minted`: Code parts rewritten in expl3 code

### Removed
- Library 'theorems': `\tcbmaketheorem` removed which is deprecated since version 2.40 (2013/07/15).
  Use `\newtcbtheorem` instead.

### Fixed
- Library `documentation`: Inconsistent local/global assignment corrected (issue #144)
- Documentation: Changed bibtex link corrected (issue #145)
- Library `breakable`: Option `use color stack` was order dependant (issue #157)
- Library `raster`: Numbering for rasters inside rasters
- In certain situations options were set twice



## [4.51] - 2021-06-14

### Changed
- Library `documentation`: Package loading of `marvosym` and `pifont`
    removed. Symbols are accessed directly now by `documentation`.

### Fixed
- Allocation error for write registers



## [4.50] - 2021-05-21

### Added
- Library `skins`: Option `opacitybacklower`
- Library `skins`: Option `bicolor jigsaw`
- Library `skins`: Option `bicolorfirst jigsaw`
- Library `skins`: Option `bicolormiddle jigsaw`
- Library `skins`: Option `bicolorlast jigsaw`
- Library `theorems`: Option `theorem hanging indent` (issue #126)

### Changed
- Documentation: Using group around arguments for title in the examples (issue #125)
- Documentation: Recommend to use initialization options after loading hyperref (issue #135)
- Documentation: Warn user about white title color becoming invisible
         for the skin `empty` (issue #118)
- Documentation: Corrections (issue #127)      
- Documentation of library `skins` is split into a general part and the catalog of skins
- Allocate write registers `\tcb@out` and `\tcb@record@out` only when needed (issue #134)
- `\tcblistof` enhanced to take an optional short title and mimic
  `\listoffigures` where applicable (issue #124)
- Library `skins`: Implementation of bicolor overhauled
- Skin documentation complemented with sidebyside examples
- Library `vignette`: Documentation examples for fading styles for every side added (issue #136)
- Library `raster`: `\thetcbrasternum` changed to output the content of a counter (issue #119)
- LaTeX counter `tcbrasterrow`, `tcbrastercolumn`, `tcbrasternum` documented.



## [4.42] - 2020-10-09

### Added
- Library `breakble`: Option `use color stack`

### Changed
- Due to several problems with the color algorithm introduced with version 4.32,
  essentially reversion to the proven pre 4.32 method.
  - support of luacolor persists (since 4.32)
  - color stacks (by pdfcol) are not mandatory any more,
    but are optional now with `use color stack`. Note that effects of whatsits
    on the vertical space have to be expected.



## [4.41] - 2020-09-29

### Fixed
- Color bleeding for xelatex and breakable boxes (since 4.32) (issue #120)



## [4.40] - 2020-09-25

### Added
- Support `hbox` for `minted` listings (issue #2)
- New default vertical space options (issue #115)
  - Option `before skip balanced`
  - Option `after skip balanced`
  - Option `beforeafter skip balanced`
  - NOTE: These options replace the current default options
        `parskip`, `noparskip`, `autoparskip`
  - WARNING: Old documents may need adapted manual page breaks where used.
           Otherwise: Use `\tcbsetforeverylayer{autoparskip}`
           to restore the old behavior!

### Changed
- `capture=hbox` applies `\@parboxrestore` now to allow e.g. hbox style
    listings inside indented environments like itemize (issue #113)
- `before skip` and `before skip balanced` do not insert glue now, if
  the tcolorbox is the first element in a minipage (or sourrounding tcolorbox)

### Deprecated
- Option `parskip`
- Option `noparskip`
- Option `autoparskip`

### Fixed
- `IfBooleanT`, `IfBooleanF` (issue #114)
- `widget` set `toprule at break` and needed the breakable library (issue #117)
- `marker` set `breakable` and needed the breakable library



The following entries are following the old style (no Markdown, switched timeflow)
==================================================================================


(2006-2011): pre publication usage

version 1.00 (2011/12/08): initial public release

version 1.01 (2012/01/26):
- dates amended to \RequirePackage(s)
- provision of the tcolorbox.tds.zip file for easier installation

version 1.02 (2012/02/15)
- documentation language changed from German to English
- small correction of the theorem title line appearance

version 1.10 (2012/03/01)
- tcblatex style for listings changed (nolol added)
- improved hyperref support
- new keys parskip and noparskip
- source code of the documentation added
- new library 'documentation' to support LaTeX documentations
  with several library commands, environments and keys (see documentation)

version 1.20 (2012/03/16)
- new geometry keys:
  'lefttitle', 'leftupper', 'leftlower', 'righttitle', 'rightupper', 'rightlower'
  and implementation changed for 'left' and 'right'
- implementation for tcolorbox changed (adaption to height options)
- new fixed height option keys:
  'natural height', 'height', 'equal height group', 'minimum for equal height group',
  'space', 'space to upper', 'space to lower', 'space to both', 'split',
  'valign', 'valign lower',
  'adjusted title'
- new bounding box option keys:
  'enlarge top by', 'enlarge bottom by', 'enlarge left by', 'enlarge right by',
  'toggle enlargement'
- preparations for a future skin changing option implemented
- commands \brackets and \docAuxCommand added to the documentation library
- documentation rearranged

version 1.30 (2012/04/20)
- several internal code changes to provide a 'skin' exchange mechanism
- new keys for the core package:
  'frame engine', 'interior titled engine', 'interior engine', 'segmentation engine'
  'skin', 'graphical environment', 'geometry nodes', 'colupper', 'collower'
- tcolorbox now defined as 'long' macro
- new keys for the library 'listings':
  'comment', 'listing and comment', 'comment and listing'
- new library 'skins' with the skins
  'standard', 'enhanced', 'freelance', 'bicolor', 'beamer', 'widget'
- keys for the library 'skins':
  'frame style', 'interior style', 'segmentation style'
  'frame code', 'interior titled code', 'interior code', 'segmentation code',
  'colbacklower'

version 2.00 (2013/03/01)
- breaking news: the new library 'breakable' adds breaking support to tcolorbox.
- e-TeX now used instead of calc
- new key 'adjust text' and new implementation for 'adjusted title'
- new geometry keys:
  'toprule', 'toprule at break', 'bottomrule', 'bottomrule at break',
  'leftrule', 'rightrule', 'titlerule', 'outer arc', 'auto outer arc',
  'toptitle', 'bottomtitle'
- new bounding box keys:
  'enlarge top at break by', 'enlarge bottom at break by'
- new overlay keys:
  'overlay', 'no overlay', 'overlay broken', 'overlay unbroken',
  'overlay first', 'overlay middle', 'overlay last',
  'overlay unbroken and first', 'overlay middle and last'
- new key: 'parbox' to change text behaviour
- new library 'breakable' for breakable boxes with the new keys:
  'breakable', 'unbreakable', 'title after break', 'notitle after break',
  'adjusted title after break', 'lines before break', 'shrink break goal'
- new keys for the 'skins' library
  'skin first', 'skin middle', 'skin last', 'title engine', 'pathfirst',
  'pathmiddle', 'pathlast', 'title style', 'title code', 'enhancedfirst',
  'enhancedmiddle', 'enhancedlast', 'enhanced', 'marker', 'bicolor',
  'bicolorfirst', 'bicolormiddle', 'bicolorlast', 'beamer',
  'beamerfirst', 'beamermiddle', 'beamerlast', 'draft', 'freelance', 'standard'
- NOTE: skins 'beamer' and 'widget' changed
  use the new style options 'beamer' and 'widget' to get the old appearance
- new watermark keys:
  'watermark text', 'watermark text on', 'watermark graphics',
  'watermark graphics on', 'watermark tikz', 'watermark tikz on',
  'no watermark', 'watermark opacity', 'watermark color',
  'watermark zoom', 'watermark stretch'

version 2.01 (2013/03/07)
- bug fix: superfluous vertical space for a breakable box which appeared after a page break
- bug fix: height computation error when a broken boxed starts with a segmentation line
- new key for the 'listings' library:
  'listing inputencoding'
- new library 'listingsutf8' as variant of 'listings' with new key
  'listing utf8'
- keys 'toprule at break', 'bottomrule at break',
  'enlarge top at break by', 'enlarge bottom at break by'
  moved from core package to 'breakable' library.
- new keys for the 'breakable' library:
  'topsep at break', 'bottomsep at break', 'pad before break',
  'pad after break', 'pad at break'

version 2.02 (2013/03/13)
- minor bug fix: segmentation line of 'enhanced' now matches 'standard'
- new macro '\tcbox' to draw a colorbox fitted to the content width
- new key 'autoparskip' to detect usage of package parskip automatically
- new key 'nobeforeafter'
- new macro '\tcbline' in the 'skins' library to draw 'just lines'
- new key 'colbacktitle' for the 'skins' library

version 2.10 (2013/04/09)
- bug fix: \tcbox ignored font settings
- outdated documentation in German removed from package
- new core package keys:
  'oversize', 'tcbox raise', 'tcbox raise base',
  'before title', 'after title', 'before upper', 'after upper', 'before lower',
  'after lower', 'center title', 'center upper', 'center lower',
  'tabularx*', 'tabularx', 'tikz upper', 'tikz lower',
  'shrink tight', 'extrude left by', 'extrude right by', 'extrude top by',
  'extrude bottom by', 'extrude by'
- the 'theorems' library now loads 'amsmath'
- new macros for the 'theorems' library:
  '\tcboxmath', '\tcbhighmath'
- new keys for the 'theorems' library:
  'math upper', 'math lower', 'math', 'highlight math', 'highlight math style',
  'ams equation upper', 'ams equation lower', 'ams equation', 'ams equation* upper',
  'ams equation* lower', 'ams equation*', 'ams align upper', 'ams align lower',
  'ams align', 'ams align* upper', 'ams align* lower', 'ams align*',
  'ams gather upper', 'ams gather lower', 'ams gather', 'ams gather* upper',
  'ams gather* lower', 'ams gather*',
  'ams nodisplayskip upper', 'ams nodisplayskip lower', 'ams nodisplayskip'
- new library 'hooks' for hook options with the new keys:
  'before upper app', 'before upper pre', 'after upper app', 'after upper pre',
  'before lower app', 'before lower pre', 'after lower app', 'after lower pre',
  'before title app', 'before title pre', 'after title app', 'after title pre',
  'before app', 'before pre', 'after app', 'after pre',
  'overlay unbroken app', 'overlay unbroken pre', 'overlay first app', 'overlay first pre',
  'overlay middle app', 'overlay middle pre', 'overlay last app', 'overlay last pre',
  'overlay app', 'overlay pre', 'overlay broken app', 'overlay broken pre',
  'overlay unbroken and first app', 'overlay unbroken and first pre',
  'overlay middle and last app', 'overlay middle and last pre',
  'watermark tikz app', 'watermark tikz pre', 'watermark tikz app on', 'watermark tikz pre on',
  'watermark graphics app', 'watermark graphics pre', 'watermark graphics app on', 'watermark graphics pre on',
  'watermark text app', 'watermark text pre', 'watermark text app on', 'watermark text pre on',
  'frame code app', 'frame code pre', 'interior titled code app', 'interior titled code pre',
  'interior code app', 'interior code pre', 'segmentation code app', 'segmentation code pre',
  'title code app', 'title code pre'
- colorization of source code snippets in the documentation

version 2.20 (2013/04/17)
- bug fix: problem with breaking boxes after headings
- new feature: support for boxes with side by side content
- new keys:
  'sidebyside', 'sidebyside align', 'sidebyside gap',
  'lefthand width', 'righthand width', 'lefthand ratio', 'righthand ratio'
- key 'nofloat' documented
- new keys for the 'listings' library:
  'listing side text', 'text side listing'
  'listing outside text', 'text outside listing'
- new keys for the 'skins' library:
  'frame hidden', 'interior hidden', 'segmentation hidden', 'title hidden'
- new environments for the 'documentation' library:
  'dispExample*', 'dispListing*'
- the default style for 'highlight math' is changed to have no title
- minor change of internal width computation
- minor internal fixes
- slight overhaul of the documentation

version 2.21 (2013/04/23)
- bug fix: \tcbox and 'sidebyside' needed 'breakable' library
- bug fix: library 'tcbhooks' relied on etoolbox package
- bug fix: breaking boxes between upper part and box frame
- new macro '\newtcolorbox'
- new macro '\newtcblisting' for the 'listings' library
- new key 'code'
- documentation corrections and extensions

version 2.22 (2013/05/15)
- bug fix: text color bleeded out of the box in some cases
- bug fix: breakable boxes were too large in some cases (leading to blank pages)
- bug fix: breaking boxes produced empty boxes in some cases
- documentation forgot naming package 'colortbl' for the 'tabularx' option
- new feature: breakable boxes allow footnotes now (like minipages)
- new macro '\newtcbox'

version 2.30 (2013/06/04)
- bug fix: handling of 'before' and 'after' for \tcbox corrected
- \tcbline now also works for centered environments
- implementation for \tcbox made more efficient
- new capture mode for automated content fit by font size adjustment
  with the new macros '\tcboxfit' and '\newtcboxfit'
  and the new keys 'fit', 'fit to', 'fit to height', 'fit basedim', 'fit skip',
  'fit maxstep'
- new keys 'baseline', 'capture', 'hbox', 'minipage'
- new stackable borderlines with the 'skins' library:
  'borderline', 'no borderline'
- new keys for the 'skins' library:
  'enhanced standard', 'blank'
- new key 'index format' for the 'documentation' library

version 2.31 (2013/06/18)
- several internal changes
- library loading mechanism revisited
- internal label change for '\tcbmaketheorem'
- new library options 'most' and 'all'
- \tcbline now also works for ragged environments
- new keys:
  'flushleft title', 'flushleft upper', 'flushleft lower',
  'flushright title', 'flushright upper', 'flushright lower'
- new key 'no listing options' for the 'listings' library
- new shadow features for the 'skins' library with the options:
  'shadow', 'fuzzy shadow', 'drop shadow', 'drop fuzzy shadow', 'halo', 'fuzzy halo'
- shadows for the 'beamer' skin changed to fuzzy
- new library 'fitting' for the content fit operations.
  NOTE: '\tcboxfit' and the fit options introduced in version 2.30 are moved
        to this new library
- the fit algorithm is completey revisited and extended
- new macro '\tcbfontsize' ('fitting library') for relative font sizes
- new keys for the 'fitting' library:
  'fit fontsize macros', 'fit height plus', 'fit width plus',
  'fit width from', 'fit height from'

version 2.32 (2013/06/23)
- bug fix: 'ams nodisplayskip lower' was applied to upper.
- new option 'check odd page'
- new environments for the 'skins' library:
  'tcbclipinterior', 'tcbclipframe', 'tcbcliptitle'
- new keys for the 'skins' library:
  'watermark overzoom', 'clip watermark'
  'clip title', 'clip upper', 'clip lower'
- NOTE: watermarks are now clipped by default.
  To get the old behaviour add the option 'clip watermark=false'

version 2.33 (2013/07/04)
- new options 'phantom', 'step and label', 'nophantom',
  'lower separated', 'reset', 'toggle left and right'
- 'highlight math' sets 'notitle,nophantom' automatically
- hyper anchor setting for theorems and LaTeX examples improved
- new key 'shield externalize' for externalization
- additional empty-first-box test for breakable boxes
- new key 'enlargepage' for fine-tuning breakable boxes
- parameter added to option 'oversize'
- option 'toggle enlargement' has a default value 'evenpage' now

version 2.40 (2013/07/15)
- bug fix: wrong footnote text width for breakable boxes
- bug fix: watermarks were influenced by baseline settings
- package etoolbox is now loaded by default
- 'phantom' changed to be stackable (!)
- introducing the new initialization option type for easy
  numbering and list generation. New options:
  'use counter', 'auto counter', 'use counter from',
  'no counter', 'number within', 'number format', 'number freestyle',
  'list inside', 'list type'
- '\newtcolorbox' and 'newtcbox' take initialization options now
- new macros '\tcblistof', '\tcbsetmanagedlayers'
- introducing the layered box concept for boxes in boxes improvement:
  * boxes inside boxes are automatically reset to default values
  * new option 'every box', 'every box on layer x', 'every box on higher layers'
  * support for footnotes for boxes in boxes (default: up to layer 4)
- new options 'step', 'label', 'list entry', 'add to list'
- library 'listings':
  * '\newtcblisting' takes initialization options now
  * new macro '\newtcbinputlisting'
- library 'theorems':
  * '\tcbmaketheorem' takes initialization options now
  * new macro '\newtcbtheorem'
- library 'fitting':
  * 'newtcboxfit' takes initialization options now
- library 'documentation':
  * the \ref... macros suppress the page numbers now if on the same page
  * new macros '\refCom*', '\refEnv*', '\refKey*'
  * docCommand and docEnvironment take options now

version 2.41 (2013/07/23)
- NOTE: The deprecated macro '\tcbmaketheorem' is redefined to its signature
  of v2.33 and before to ensure backward compatibility. This may break code
  written with v2.40 using '\tcbmaketheorem'.
- minor internal improvements
- support for the cleveref package with
  * new initialization options 'crefname', 'Crefname'
  * new options 'label type', 'no label type'
- library 'theorems':
  * new options: 'separator sign', 'separator sign colon', 'separator sign dash'
- library 'listings':
  * capture mode can be changed for 'tcblisting' and '\tcbinputlisting'
  * new option: 'listing remove caption'

version 2.50 (2013/07/29)
- first line indent corrected for 'parbox=false'
- minor internal improvements
- new option keys
  'height plus', 'height from'
- new library 'minted' with support for the minted package (Pygments support)
  * new options 'minted language', 'minted options', 'minted style'
- new library option 'many'
- new common listings options:
  'listing engine'
- library 'documentation':
  * new options 'documentation minted style', 'documentation minted options'

version 2.51 (2013/09/16)
- bug fix: processing of 'initialization option keys' fixed
  for \newtcbox, \newtcbinputlisting, and \newtcboxfit
- bug fix: disturbing horizontal space in \tcboxfix removed
- new macros '\renewtcolorbox', '\renewtcbox'
- library 'skins':
  * implementation for the skin families 'enhanced', 'beamer', and 'bicolor' changed
  * break sequence changed for skin 'freelance'
  * new skins: 'freelancefirst', 'freelancemiddle', 'freelancelast'
  * new options: 'extend freelance', 'extend freelancefirst',
    'extend freelancemiddle', 'extend freelancelast',
    'drop midday shadow', 'drop fuzzy midday shadow'
  * new environment 'tcbinvclipframe'
- library 'listings':
  * new macros '\renewtcblisting', '\renewtcbinputlisting'
- library 'theorems':
  * new macro '\renewtcbtheorem'
- library 'fitting':
  * new macro '\renewtcboxfit'
- library 'documentation':
  * new option 'documentation listing options'

version 2.60 (2013/12/17)
- new 'jigsaw' variants for the skins 'standard' and 'enhanced' for
  advanced transparency and similar effects.
- new package core skin 'standard jigsaw'
- 'tabularx' and 'tabularx*' reset the arrayrulecolor to black after the table now.
- option 'colbacktitle' moved from library 'skins' to package core
- new options:
  'title filled', 'opacityupper', 'opacitylower', 'opacitytitle', 'opacityframe',
  'opacityback', 'opacitybacktitle', 'opacityfill', 'opacitytext','hyphenationfix',
  'standard jigsaw', 'enlarge by', 'grow to left by', 'grow to right by'
- library 'skins':
  * new skin: 'enhanced jigsaw', 'enhancedfirst jigsaw', 'enhancedmidle jigsaw',
    'enhancedlast jigsaw'
  * marker style now based on 'enhancedmiddle jigsaw'
  * new options:
  'enhanced jigsaw', 'tikz', 'tikz reset', 'show bounding box',
  'at begin tikz', 'at begin tikz reset', 'at end tikz', 'at end tikz reset',
  'rotate', 'scale', 'remember', 'remember as',
  'drop shadow southeast', 'drop shadow south', 'drop shadow southwest', 'drop shadow west',
  'drop shadow northwest', 'drop shadow north', 'drop shadow northeast', 'drop shadow east',
  'drop fuzzy shadow southeast', 'drop fuzzy shadow south', 'drop fuzzy shadow southwest',
  'drop fuzzy shadow west', 'drop fuzzy shadow northwest', 'drop fuzzy shadow north',
  'drop fuzzy shadow northeast','drop fuzzy shadow east',
- library 'listings':
  new options 'text above listing' and 'listing above text'
- library 'theorems':
  \newtcbtheorem creates an additional starred theorem environment
- library 'fitting':
  fit algorithm warning switched off by default.
  new options:
  'fit warning'
- library 'documentation': more values for 'index format'
- documentation extended
- major internal implementation changes and optimizations

version 2.61 (2014/01/10)
- bug fix: '@' was set as letter in some situations
- typing error corrections
- new macro \tcbsetforeverylayer
- library 'skins':
  * new macros and environments:
    '\tcbstartdraftmode', '\tcbstopdraftmode', '\tcbinterruptdraftmode', '\tcbcontinuedraftmode'
  * new skin: 'spartan'
  * new options: 'spartan', 'draftmode'
- library 'fitting':
  * alternative fitting algorithms implemented (fontsize, areasize, hybrid, squeeze)
  * new option: 'fit algorithm'

version 2.70 (2014/02/06)
- bug fix: global setting of 'before' or 'after' may produce errors or
           side effects for layered boxes.
- compatibility issue with TikZ 3.00 solved
- new options:
  'detach title', 'attach title', 'attach title to upper',
  'tikznode upper', 'tikznode lower', 'tikznode'
- library 'theorems':
  * new options:
  'separator sign none', 'terminator sign', 'terminator sign colon',
  'terminator sign dash', 'terminator sign none', 'description delimiters',
  'description delimiters parenthesis', 'description delimiters none',
  'theorem name and number', 'theorem number and name', 'theorem name',
  'theorem style'
- library 'documentation':
  * re-implementation of the documenting environments
    (may alter existing documents slightly)
  * new environments:
    'docCommand*', 'docEnvironment*', 'docKey*'
  * new commands:
    '\docAuxCommand*', '\docAuxEnvironment', '\docAuxEnvironment*',
    '\docValue', '\docValue*', '\docAuxKey', '\docAuxKey*',
    '\docColor*', '\refAux', '\refAuxcs'
  * new options:
    'doc left', 'doc right', 'doc left indent', 'doc right indent',
    'doc head', 'doc head command', 'doc head environment', 'doc head key',
    'doc description', 'doc into index', 'value', 'values'

version 2.71 (2014/02/21)
- bug fix: sidebyside setting with empty left hand side caused false positioning
- new options:
  'external', 'remake'
- library 'listings':
  * new options:
    'comment side listing', 'listing side comment', 'comment above listing',
    'listing above comment', 'comment outside listing', 'listing outside comment',
    'image comment',
- library 'documentation':
  * automatic inclusion of the 'skins' library
  * inclusion of 'makeidx' made dependent on the existence of '\printindex'
  * new options:
    'keys', 'index colorize', 'index annotate',
    'color command', 'color environment', 'color key', 'color value', 'color color'

version 2.72 (2014/03/18)
- bug fix: mixing \newtcblisting with 'ams align' and similar options was not possible
- bug fix: footnotes lost for 'listing outside text' and similar options
- sidebyside and outside implementation slightly changed for beamer usage
- bicolor skin respects 'opacityback' for the upper part now
- new TikZ options:
  'fill image opacity', 'fill image options',
  'fill plain image', 'fill plain image*', 'fill stretch image', 'fill stretch image*',
  'fill overzoom image', 'fill overzoom image*', 'fill zoom image', 'fill zoom image*',
  'fill shrink image', 'fill shrink image*', 'fill tile image', 'fill tile image*'
- library 'skins':
  * new options:
    'frame style image', 'frame style tile', 'interior style image', 'interior style tile',
    'title style image', 'title style tile'
- library 'listings':
  * new options:
    'every listing line', 'every listing line*'

version 2.80 (2014/03/31)
- implementation changed for all '\newtcolorbox', '\newtcbox', etc., macros.
- new option:
  'float*'
- new TikZ option:
  'fill image scale'
- library 'skins' new option:
  'watermark shrink'
- new library 'xparse' with new commands:
  '\DeclareTColorBox', '\NewTColorBox', '\RenewTColorBox', '\ProvideTColorBox',
  '\DeclareTotalTColorBox', '\NewTotalTColorBox', '\RenewTotalTColorBox', '\ProvideTotalTColorBox',
  '\DeclareTCBox', '\NewTCBox', '\RenewTCBox', '\ProvideTCBox',
  '\DeclareTotalTCBox', '\NewTotalTCBox', '\RenewTotalTCBox', '\ProvideTotalTCBox',
  '\DeclareTCBListing', '\NewTCBListing', '\RenewTCBListing', '\ProvideTCBListing',
  '\DeclareTCBInputListing', '\NewTCBInputListing', '\RenewTCBInputListing', '\ProvideTCBInputListing',
  '\DeclareTCBoxFit', '\NewTCBoxFit', '\RenewTCBoxFit', '\ProvideTCBoxFit',
  '\DeclareTotalTCBoxFit', '\NewTotalTCBoxFit', '\RenewTotalTCBoxFit', '\ProvideTotalTCBoxFit',
  '\tcboxverb'

version 3.00 (2014/05/08)
- bug fix: 'title code app', 'title code pre' changed wrong code
- documentation corrections
- implementation of graphical engines changed (!)
- note: optical backward compatibility issues with breakable 'freelance' boxes possible
- 'frame code' and similar options are moved from the 'skins' library to the core package
- 'enlarge top at break by' and 'enlarge bottom at break by' moved from 'breakable' library to the core package
- new macros:
  '\tcbnewsubskin'
- new options:
  'skin first is subskin of', 'skin middle is subskin of', 'skin last is subskin of',
  'enlarge top initially by', 'enlarge finally last by', 'overlay unbroken and last'
  'size', 'on line', 'varwidth upper',
  'frame empty', 'interior empty', 'interior titled empty', 'segmentation empty', 'title empty'
- new TikZ options:
  'tcb fill frame', 'tcb fill interior', 'tcb fill title'
  'fill plain picture', 'fill stretch picture', 'fill overzoom picture',
  'fill zoom picture', 'fill shrink picture', 'fill tile picture', 'fill tile picture*'
- library 'skins' new options (concerning 'underlay', 'finish' and 'boxed title'):
  'underlay unbroken', 'underlay first', 'underlay middle', 'underlay last',
  'underlay', 'underlay broken', 'underlay unbroken and first',
  'underlay middle and last', 'underlay unbroken and last',
  'no underlay unbroken', 'no underlay first',
  'no underlay middle', 'no underlay last', 'no underlay',
  'finish unbroken', 'finish first', 'finish middle', 'finish last',
  'finish', 'finish broken', 'finish unbroken and first',
  'finish middle and last', 'finish unbroken and last',
  'no finish unbroken', 'no finish first',
  'no finish middle', 'no finish last', 'no finish',
  'empty', 'blanker',
  'boxed title style', 'varwidth boxed title', 'varwidth boxed title*',
  'minipage boxed title', 'minipage boxed title*', 'tikznode boxed title',
  'hbox boxed title', 'boxtitle/xshift', 'boxtitle/yshift', 'boxtitle/yshifttext',
  'boxtitle/yshift*', 'attach boxed title to top left', 'attach boxed title to top center',
  'attach boxed title to top right', 'attach boxed title to bottom left',
  'attach boxed title to bottom center', 'attach boxed title to bottom right',
- new engine and skin 'empty'
- implementation of 'show bounding box' changed to be a border line.
- library 'hooks' new options:
  'underlay unbroken pre', 'underlay first pre', 'underlay middle pre',
  'underlay last pre', 'underlay pre', 'underlay broken pre',
  'underlay unbroken and first pre', 'underlay middle and last pre',
  'underlay unbroken and last pre'
  'finish unbroken pre', 'finish first pre', 'finish middle pre',
  'finish last pre', 'finish pre', 'finish broken pre',
  'finish unbroken and first pre', 'finish middle and last pre',
  'finish unbroken and last pre'
  'overlay unbroken and last app', 'overlay unbroken and last pre'
- library 'theorems':
  * new options:
  'description color', 'description font', 'description formatter'

version 3.01 (2014/05/13)
- bug fix: 'parbox=false' plus 'breakable' had an unwanted indent
- compatibility fix for tabularx 2014/04/22 v2.09

version 3.02 (2014/05/13)
- compatibility fix for tabularx 2014/04/22 v2.09 (again)

version 3.03 (2014/05/16)
- bug fix: some initialization option keys for \newtcblisting did not operate correctly
- bug fix: boxed title shape 'title' was unknown in underlays
- more boxed title example documented

version 3.04 (2014/05/18)
- compatibility fix for tabularx removed; compatible with tabularx 2014/05/13 v2.10
- boxed title improvements:
  * the 'title' node is accessible now from inside 'frame code' and 'interior code'
  * new keys 'underlay boxed title', 'no underlay boxed title', 'underlay boxed title pre'
  * documentation example updated

version 3.05 (2014/05/28)
- compatibility fix for the upcoming version 2.0 of the package minted
- inner boxes are enforced to be unbreakable now
- library 'breakable':
  new key 'enforce breakable' (for breaking inner boxed deliberately)
- library 'skins':
  * new options:
  'lifted shadow', 'drop small lifted shadow', 'drop lifted shadow', 'drop large lifted shadow'

version 3.10 (2014/07/23)
- box breaking algorithm revised:
  * breakable boxes now always have \noindent
  * distance to preceeding text corrected
  * interaction with floating objects fixed
  * dimensioning of partial boxes improved
  * splitting of an empty closing frame can now be avoided (depending on 'pad at break*')
  * The upper total height limit for breakable boxes is extended from
    about 16384pt to about 65536pt
  * experimental code added (breakable=unlimited) for breakable boxes
    without height limit besides memory
  * splitting boxes inside multicols environments supported (to a certain degree)
  * limited orphan control added ('enlargepage flexible')
- library 'breakable':
  * new options:
  'break at', 'height fixed for', 'enlargepage flexible',
  'pad before break*', 'pad at break*'
- Corners can be set individually now to be 'rounded' or 'sharp'
  for all types of boxes, skins, borders, and shadows:
  * new options:  'sharpish corners', 'sharp corners', and 'rounded corners'
- library 'skins':
  * new macros: '\tcbline*'
  * bug fix: skin families 'bicolor' and 'beamer' did not respect 'colbacktitle'
- pictures 'blueshade.png', 'crinklepaper.png', 'goldshade.png', 'pink_marble.png'
  moved to package folder

version 3.11 (2014/07/25)
- regresssion: vertical space at end of breakable boxes was not removed
- example file updated with new features

version 3.12 (2014/07/29)
- text color implementation changed to circumvent xelatex color problems
- multicol vs. twocolumn detection fixed
- code for breakable boxes without height limit improved
- before box \noindent is replaced by \parindent=0pt (bidi package compatibilty)
- library 'breakable':
  * new option: 'vfill before first'

version 3.20 (2014/09/22)
- bug fix: titles set with 'detach' or 'boxed title' options were not considered
    for lists of tcolorboxes.
- bug fix: 'extrude left by', 'extrude right by' worked only for '\tcbox' but not for 'tcolorbox'
- bug fix: 'pad before break*' and 'pad at break*' were always setting to 0pt
- new options: 'every float', 'list text', 'overlay first and middle',
  'height fill'
- new initialization options:
  'use counter*', 'blend into'
- library 'skins':
  * new macros: '\tcbsettowidthofnode', '\tcbsetmacrotowidthofnode',
    '\tcbsettoheightofnode', '\tcbsetmacrotoheightofnode'
  * new options: 'underlay first and middle', 'finish first and middle'
- library 'hooks':
  * new options: 'underlay first and middle pre',
    'overlay first and middle app', 'overlay first and middle pre',
    'finish first and middle pre'
- library 'documentation':
  * new macros: '\tcbdocmarginnote', '\tcbdocnew', '\tcbdocupdated'
  * The 'docKey' and 'docKey*' environments take tcolorbox options now
  * new options:
    'doclang/new', 'doclang/updated',
    'doc marginnote', 'doc updated', 'doc new', 'doc new and updated'

version 3.21 (2014/10/10)
- bug fix: empty key path handling inside the 'docKey' and 'docKey*' environments was faulty
- bug fix: wrong coloring for '\docAuxCommand' and '\docAuxCommand*'
- bug fix: draft mode for inner boxes deactivated in v3.20
- subtitles added
- new macros:
  '\tcbsubtitle'
- new options:
  'subtitle style', 'before skip', 'after skip', 'beforeafter skip',
- library 'documentation':
  implementation of handling macro and key names changed to accept underscores
  several internal implementation changes

version 3.22 (2014/10/31)
- new macro: '\tcolorboxenvironment'
- new options:
  'text width', 'text height'
- library 'skins':
  * new options: 'borderline north', 'borderline south',
    'borderline east', 'borderline west', 'borderline horizontal', 'borderline vertical'
- library 'breakable':
  * internal change for compatibility with the 'perpage' option of the 'footmisc' package
- library 'theorems':
  * compatibility fix: The 'ams equation' options left too much vertical
    space for the 'fleqn' case
- library 'fitting':
  * new 'fit algorithm' settings: 'fontsize*', 'areasize*', 'hybrid*'

version 3.30 (2014/11/17)
- bug fix: compilation errors using colors like 'red!10' in some skins like 'beamer'
- '\thetcbcounter' can now be used as part of a 'listing file' name for 'tcblisting'
- implementation of 'before skip' and 'after skip' improved
- implementation of 'equal height group' improved to take arbitrary id's
- Quick Reference added
- new options:
  'add to width', 'add to height',
  'box align', 'left skip', 'right skip', 'leftright skip'
- library 'skins':
  * new macros:
  '\tcbincludegraphics', '\tcbincludepdf'
  * new options:
  'graphics options', 'graphics directory', 'graphics pages'
- library 'listings', 'listingsut8', 'minted':
  * 'listing file' now usable inside 'tcblisting' and 'tcbinputlisting'
  * new options:
  'comment only', 'text above* listing', 'listing above* text',
  'comment above* listing', 'listing above* comment',
  'comment style', 'tcbimage comment', 'pdf extension', 'pdf comment',
  'process code', 'no process', 'run system command', 'run pdflatex',
  'run xelatex', 'run lualatex', 'run makeindex', 'run bibtex', 'run biber',
  'run arara', 'run latex', 'run dvips', 'run ps2pdf',
  'compilable listing'
- new library 'raster':
  * new macros and environments:
  'tcbraster', 'tcbitemize', 'tcbitem'
  * new options:
  'raster columns', 'raster rows', 'raster width', 'raster height', 'raster before skip',
  'raster after skip', 'raster left skip', 'raster right skip', 'raster column skip',
  'raster row skip', 'raster halign', 'raster valign', 'raster equal height',
  'raster equal height group', 'raster force size' ,'raster reset',
  'raster odd column', 'raster even column', 'raster column n', 'raster odd row',
  'raster even row', 'raster row m','raster odd number', 'raster even number',
  'raster row m column n', 'raster number n'

version 3.31 (2014/11/28)
- new macros: '\tcbstartrecording', '\tcbrecord', '\tcbstoprecording', '\tcbinputrecords'
- new options: 'squeezed title', 'squeezed title*', 'phantomlabel',
  'record', 'no recording'
- 'savelowerto' changed to need only one run instead of two
- library 'skins':
  * '\imagename' macro can be used in more situations
  * '\tcbincludegraphics' made aware of 'grffile' package
- new library 'raster':
  * tcbraster safeguarded against restricted horizontal mode
  * new option: 'raster every box'

version 3.32 (2014/12/01)
- bug fix for 'crefname' and 'Crefname' options (cleveref support)

version 3.33 (2014/12/11)
- The nobreak settings after a heading are respected now for breakable and
  unbreakable boxes. Use the new option 'ignore nobreak' to restore the old
  behavior.
- vertical skip of two successive tcbraster environments fixed

version 3.34 (2014/12/16)
- 'height fill' now fills gapless and can be overruled by other height options
- 'before skip' and 'after skip' accept glue values now
- library 'breakable':
  * new option 'compress page':
    Use the new option 'compress page=none' to restore the old behavior.
- library 'raster':
  * 'raster before skip' and 'raster after skip' accept glue values now

version 3.35 (2015/01/07)
- fix: 'tcbdocumentation.code.tex' changed to US-ASCII
- text color implementation changed to fix some color problems
- new options: 'upperbox', 'visible', 'invisible'
- documentation complemented

version 3.36 (2015/01/09)
- bug fix: dimension settings with 'em' or 'ex' units were sometimes converted to 0pt
- bug fix: 'boxed title' options and some algorithms of the 'fitting' library were not compatible
- bug fix: 'fit width from' ('fitting' library) may have updated counter too often
- new option: 'only'
- library 'fitting': fit process can now also includes the title
- library 'raster': new option 'raster equal skip'
- library 'documentation':
  * new macros and environments:
    '\docCounter', '\docCounter*', '\docLength', '\docLength*'
  * new options:
    'index command', 'index command name' (for imakeidx),
    'color counter', 'color length',
    'doclang/counter', 'doclang/counters', 'doclang/length', 'doclang/lengths'

version 3.40 (2015/01/14)
- bug fix: list environments had too much leading space if set as first elements in a box
- library 'skins':
  * new option: 'titlerule style'
- library 'breakable':
  algorithm for handling overfull boxes revised; new warnings implemented

version 3.50 (2015/03/16)
- bug fix: \tcbline was broken for \tcboxfit-boxes since 3.36
- text color implementation changed to fix some color problems
- before/after settings changed to detect special situations
- 'sidebyside align': new selections 'top seam', 'center seam', 'bottom seam'
- new options:
  'force nobeforeafter', 'blend before title', 'blend before title code'
- library 'documentation':
  'before example', 'after example' are deprecated; 'docexample' is changed
- new library 'external'
  * new macros and environments:
    'tcbexternal', '\tcbEXTERNALIZE', 'extikzpicture', 'extcolorbox',
    '\tcbifexternal',
    '\newtcbexternalizeenvironment', 'renewtcbexternalizeenvironment',
    'newtcbexternalizetcolorbox', 'renewtcbexternalizetcolorbox'
  * new options:
    'runner', 'externalize', 'force remake', '!',
    'name', 'externalize listing', 'externalize listing!',
    'externalize example', 'externalize example!',
    'prefix', 'environment', 'minipage', 'plain', 'compiler', 'runs',
    'input source on error', 'safety', 'preamble'
- documentation structure revised

version 3.60 (2015/05/07)
- bug fix: dimension settings with 'em' or 'ex' units for 'enlarge .. by' converted to 0pt
- bug fix: 'bicolor' skin sometimes ignored color for lower part when broken
- new macros: '\tcbpatcharcangular', '\tcbpatcharcround'
- implementation of text alignment changed with new options:
  'halign', 'halign upper', 'halign lower', 'halign title', 'valign upper'
- new options:
  'saveto', 'circular arc', 'bean arc', 'arc is angular', 'arc is curved',
  'square', 'tcbox width'
- library 'skins':
  * new option: 'smart shadow arc'
- library 'documentation':
  package 'doc' removed from list of required packages
- library 'external':
  * new options:
    'environment with percent', 'preamble tcbset', 'preclass', 'clear preclass',
    'PassOptionsToPackage', 'PassOptionsToClass'

version 3.61 (2015/06/12)
- bug fix: nobreak settings after a heading were sometimes ignored depending
  on the box content
- library 'external':
  * now throws an error if the same external job name is used twice
  * new option: '-'
- documentation bug fixes

version 3.70 (2015/07/16)
- bug fix: 'attach title to upper' attached also empty titles
- bug fix: library 'raster': blank line after tcbitemize or tcbraster could give an error message
- new options:
  'text fill', 'valign scale bound',
  'valign=scale', 'valigns=scale*', 'valign lower=scale', 'valign lower=scale*'
- library 'breakable':
  * Settings for broken box parts are now shielded by TeX grouping. This may
    break code which used side-effects with unproper skins.
  * new options:
    'extras unbroken', 'extras first', 'extras middle', 'extras last',
    'extras', 'extras broken', 'extras unbroken and first',
    'extras unbroken and last', 'extras middle and last',
    'extras first and middle', 'no extras unbroken', 'no extras first',
    'no extras middle', 'no extras last', 'no extras',
- library 'hooks':
  * new options:
    'extras unbroken pre', 'extras first pre', 'extras middle pre',
    'extras last pre', 'extras pre', 'extras broken pre',
    'extras unbroken and first pre', 'extras unbroken and last pre',
    'extras middle and last pre', 'extras first and middle pre',
- new library 'magazine'
  * new macros and environments:
    '\newboxarray', '\boxarraygetsize', '\boxarrayreset', '\boxarrayclear',
    '\boxarraygetbox', '\boxarraygetwidth', '\boxarraygetheight', '\boxarraygetdepth',
    '\boxarraygettotalheight', '\useboxarray', '\usetcboxarray',
    '\consumeboxarray', '\consumetcboxarray', 'boxarraystore',
  * new options:
    'store to box array', 'reset box array', 'do not store to box array',
    'reset and store to box array'

version 3.71 (2015/07/23)
- bug fix: An error introduced in 3.70 broke all code without 'breakable' library
- bug fix: library 'external': spurious blank in source input removed
- documentation extended

version 3.72 (2015/08/12)
- bug fix: bounding box changes and boxed title additions were not considered
    correctly by 'height fixed for' or 'height fill' (resulting in wrong page breaks)
- library loading made compatible with expl3
- cosmetic documentation changes

version 3.73 (2015/10/16)
- bug fix: '\tcbdocmarginnote' had a spurious blank.
- parbox=false settings adapted for embedded lists
- library 'documentation':
  * new options:
  'before doc body command', 'after doc body command',
  'before doc body environment', 'after doc body environment',
  'before doc body key', 'after doc body key',
  'before doc body', 'after doc body'

version 3.80 (2015/11/27)
- superfluous and sometimes troublesome \unskip's were removed.
  Note that this changed the behavior of 'after upper' and 'after lower'.
  Some user code may need to apply the new 'after upper*' / 'after lower*'
  options or insert an \unskip.
- even/odd page testing completely rewritten.
- some difference formulas were revised.
- new macros:
  '\thetcolorboxnumber', '\thetcolorboxpage',
  '\tcbifoddpage', '\tcbheightfromgroup'
- new options:
  'after upper*', 'after lower*',
  'center', 'flush right', 'flush left',
  'if odd page', 'if odd page*',
  'use height from group'
- library 'xparse':
  * new macro:    '\tcbsidebyside'
  * new options:  'sidebyside adapt', 'sidebyside switch'

version 3.90 (2016/02/29)
- bug fix: 'height fill' after headings (nobreak) produced an error
- implementation for 'before' and 'before skip' changed to avoid spacing
  problems when there is a page break before breakable/unbreakable boxes
- the 'height fill' option can be applied also for boxed inside a tcbraster
- new options:
  'add to natural height', 'space to', 'use height from group' (new default)
- new macros:
  '\tcbheightspace', '\tcbtextwidth', '\tcbtextheight'
- library 'skins':
  * 'halign title' works with 'boxed title' now
  * 'boxed title style' changed to be stackable
  * better support for titles at the bottom of the box
  * new skin: 'tile'
  * new options:
    'blankest', 'tile', 'no boxed title style', 'boxed title size',
    'attach boxed title to bottom', 'attach boxed title to bottom*',
    'attach boxed title to top', 'attach boxed title to top*',
    'flip title'
- library 'raster':
  * new environment:
    'tcboxedraster'
  * new options:
    'raster multicolumn', 'raster multirow'
- library 'documentation':
  removal of some unwanted blanks

version 3.91 (2016/04/27)
- bug fix: '\tcbline' was indented when setting '\parindent' inside a box
- bug fix: 'minimum for equal height group' changed current equal height group
    and settings with 'em' or 'ex' units were converted to 0pt
- bug fix: setting '-output-directory' and 'outputdir=' for the minted package
    broke \tcblisting for 'listing engine=minted'
- documentation: biber problem with latin1 encoding circumvented
- new options:
  'minimum for current equal height group'
- library 'theorems':
  * new option: 'label separator'
- new library 'vignette' for ornamental frames:
  * new fadings: 'semi west', 'semi east', 'semi north', 'semi south'
  * new macros: '\tcbvignette'
  * new options:
    'xmin', 'xmax', 'ymin', 'ymax',
    'lower left corner', 'upper right corner', 'inside node', 'outside node',
    'over node', 'over node offset', 'north size', 'south size', 'east size',
    'west size', 'size', 'north style', 'south style', 'east style', 'west style',
    'draw method', 'fade out', 'semi fade out', 'fade in', 'semi fade in',
    'base color', 'raised color', 'lowered color',
    'underlay vignette', 'underlay raised fading vignette',
    'underlay raised shading vignette', 'underlay shade in vignette',
    'finish vignette', 'finish raised fading vignette', 'finish fading vignette'
- library 'raster':
  * new environment: 'tcboxeditemize'

version 3.92 (2016/05/28)
- bug fix: 'compilable listing' used no '.tex' extension causing problems with minted
- compatibility patch for \vsplit in luatex 0.95 causing problems with breakable boxes
- settings inside \tcbvignette are now inside a group
- library 'vignette': new option 'scope'

version 3.93 (2016/06/01)
- bug fix: compatibility patch for \vsplit in luatex 0.95 was buggy
- system commands are now accessed using the 'shellesc' package for
  compatibility with luatex

version 3.94 (2016/07/14)
- bug fix: '\tcbincludegraphics' for fixed height boxes was broken since v3.90 (2016/02/29)
- new option 'nameref'
- library 'theorems':
  Theorems made nameref-aware
- library 'listings':
  * new options:
  'freeze file', 'freeze none', 'freeze extension',
  'freeze pdf', 'freeze png', 'freeze jpg'
- library 'external':
  * implementation improved for lualatex and xelatex
  * new macro '\tcbiffileprocess'

version 3.95 (2016/10/21)
- The behaviors of 'after upper' and 'after lower' are reverted back to
  prior version 3.80 to have an automatic \unskip inserted.
  Therefore, 'after upper*' and 'after lower*' are deprecated now.
- new option 'void'
- library 'skins':
  '\tcbincludegraphics' made compatible with 'height fill' boxes.
- library 'minted':
  now, included source files are searched for in relation to an optional
  'output-directory' and also locally.
- library 'documentation':
  Language settings are not longer reset to English for embedded boxes.

version 3.96 (2016/11/18)
- bug fix: unprotected definition of the 'nameref' option induced serious errors
- bug fix: nameref package was not detected if loaded after tcolorbox
- new macros:
  '\tcbifoddpageoroneside'
- new options:
  'if odd page or oneside', 'if odd page or oneside*',
- library 'documentation':
  * Documentation options are not longer reset to default values for embedded
    boxes. User code may be affected by this change.
  * marginnotes adapt to twosided documents now

version 4.00 (2017/02/16)
- Code adaptions to support \parfillskip changing packages like KOMA-Script:
  'parskip', 'noparskip', 'after skip', 'breakable', 'raster'
- 'toggle left and right' toggles corners now
- new options:
  'left*', 'right*',
  'spread inwards', 'spread outwards', 'move upwards', 'move upwards*', 'fill downwards',
  'spread sidewards', 'spread upwards', 'spread upwards*', 'spread downwards', 'spread',
  'hypertarget', 'bookmark', 'bookmark*'
- library 'skins':
  * new macro '\tcbhypernode'
  * new options:
  'hyperref', 'hyperref node', 'hyperref interior', 'hyperref title',
  'hyperlink', 'hyperlink node', 'hyperlink interior', 'hyperlink title',
  'hyperurl', 'hyperurl node', 'hyperurl interior', 'hyperurl title',
  'hyperurl*', 'hyperurl* node', 'hyperurl* interior', 'hyperurl* title'

version 4.01 (2017/02/19)
- bug fix: 'raster halign=center' was broken by 4.00 code changes

version 4.02 (2017/02/24)
- Further code adaptions to support \parfillskip changing packages like KOMA-Script
  and to respect center environments
  'parskip', 'noparskip', 'after skip', 'breakable', 'raster'
- new option: 'parfillskip restore'
- bug fix: 'segmentation style' was not applied correctly to breakable boxes with
  'bicolor' skin
- bug fix: '/tcb/external/!' and '/tcb/external/-' were not usable inside \tcbset
- documentation optimizations

version 4.03 (2017/04/25)
- Implementation of 'raster equal height' changed to be more robust e.g. for loops
- Implementation of several fill options like 'fill stretch image' changed
  to be more efficient and to be independent from TikZ node positioning options.
- Bug fix: 'fill plain image' and 'fill plain picture' ignored 'fill image opacity'.
- new macro: '\tcbsegmentstate'
- library 'breakable':
  * new option: 'segmentation at break'
- library 'documentation':
  * new options: 'documentation minted language', 'keywords bold'
- Creation of leaflets documented

version 4.10 (2017/07/05)
- new options:
  'inherit height', 'verbatim ignore percent'
- library 'skins'
  * new style 'enhanced standard jigsaw'
- library 'magazine':
  * new macro: '\ifboxarrayempty'
- library 'breakable':
  * option 'break at' allows negative values now.
  * the algorithm for breaks inside a multicolumn environment was improved
    (user code may be affected by this change).
  * new macro: '\tcbbreak'
- library 'minted':
  * the default settings for 'minted options'
    are supplemented by 'breaklines,autogobble'
- new library 'poster'
  * new macros and environments:
    'tcbposter',  '\tcbposterset', '\posterbox', 'posterboxenv',
    'tcbposterwidth', 'tcbposterheight', 'tcbpostercolspacing', 'tcbposterrowspacing',
    'tcbpostercolumns', 'tcbposterrows', 'tcbpostercolwidth', 'tcbposterrowheight'
  * new options:
    'poster', 'columns', 'rows', 'colspacing', 'rowspacing', 'spacing',
    'showframe', 'width', 'height', 'prefix', 'coverage', 'no coverage',
    'boxes', 'fontsize', 'name', 'column', 'column*', 'span', 'row', 'rowspan',
    'fixed height', 'below', 'above', 'at', 'between', 'sequence',
    'placeholder', 'xshift', 'yshift'
- New example file 'tcolorbox-example-poster'
- New tutorial 'tcolorbox-tutorial-poster' for poster creation

version 4.11 (2017/09/14)
- Standard internal minipage settings changed from 'c' to 'b' which should
  fix some glitches

version 4.12 (2018/01/12)
- color implementation changed to fix problems with expl3 (thanks to Ulrike Fischer)
- Documentation typo corrected ('tcbsetmanagedlayers' instead of 'tcbsetmanagedlayer')
- Bug fix: 'borderline south' and 'borderline north' created 'Missing character'
  messages for breakable boxes
- library 'theorems':
  * new options 'theorem label supplement', 'theorem full label supplement'

version 4.13 (2018/03/22)
- typos in 'tcolorbox-tutorial-poster' corrected
- new options:
  'grow sidewards by'
- library 'breakable':
  * Warning for discarded zero height box content added
- library 'listings':
  * Documentation for 'text side listing', 'listing side text',
    'comment side listing', 'listing side comment' supplemented with notes.
- library 'skins':
  * Options given by '/tcb/graphics options' and '/tikz/fill image options'
    are now fully expanded while applied to underlying '\includegraphics'
  * new option:
    'graphics orientation'

version 4.14 (2018/07/26)
- bug fix (#40): 'tikz lower' and 'tikz upper' failed to take more than one parameter
- '\tcblistof' issues a warning if tocdepth is lower than 1 (#42)
- macro definition of \tcolorbox@label removed from aux file (#47)
- documentation adapted to the changed argument collection of the xparse package (#43)
- new options: 'index', 'index*'
- library 'breakable':
  * (#41) 'title after break' inherits the title alignment now
    (may change output of existing documents!)
  * new options 'extras title after break', 'no extras title after break'

version 4.15 (2018/12/07)
- bug fix (#40): 'tikz upper', 'tikz lower' failed to take more than one parameter (again)
- bug fix: 'tcboxedraster' could not be set to be 'breakable'
- library 'breakable': Implementation of 'pad after break' changed to be
  consistent with a boxed title.
- library 'raster':
  * dimension settings changed to be more robust
  * new options (#52) 'raster width center', 'raster width flush left', 'raster width flush right'
- Example source code of 'tcolorbox-example-poster' and 'tcolorbox-tutorial-poster'
  adapted to be compatible with lipsum package version 2.0

version 4.20 (2019/03/02)
- bug fix (#60): \multicolumn could not be used for first cell with option 'tabularx'
- internal colors names renamend and offially documented (Section 9.5 Color Names):
  'tcbcolframe', 'tcbcolback', 'tcbcolbacktitle', 'tcbcolbacklower',
  'tcbcolupper', 'tcbcollower', 'tcbcoltitle'
- listingsutf8 compatability better documented (#58)
- semantic changed for options: 'after upper*', 'after lower*'
- new options: 'before upper*', 'before lower*', 'titlebox', 'nirvana'
- library 'skins':
  * new options: 'beamer hidden', 'beamer alerted', 'hide', 'alert'
  * option 'only' moved from package to skins library
- new documentation section '13 Beamer Support'

version 4.21 (2019/09/19)
- bug fix (#71): 'shield externalize' should be effective on all tcolorbox layers
- bug fix (#76): 'spread inwards', 'spread outwards', 'spread sidewards' gave
  wrong results for some document geometry settings
- new options (#75): 'tabulars', 'tabulars*'
- library 'extras':
  * bug fix: all 'extras ...' options from library 'hooks' took code instead of options
  * new options (#73): 'minted options app', 'minted options pre',
      'listing options app', 'listing options pre'
- library 'xparse':
  * bug fix: options 'IfNoValueTF', 'IfValueTF', 'IfBooleanTF' failed
      to recognize arguments in some code line breaks situations
- library 'documentation':
  TikZ path operation documentation (#65):
  * new color name: 'Fade'
  * new macros and environments: '\colFade', 'docPathOperation',
      '\refPathOperation', '\refPathOperation*'
  * new options: 'color fade', 'color path', 'doc label', 'doc head path',
      'before doc body path', 'after doc body path'
  * new language string: 'path', 'paths'
- documentation: checkerbox for opacity examples was too dark

version 4.22 (2019/11/15)
- bug fix (#79) in library 'xparse':
  'sidebyside adapt' did not respect color, font, and other options.
- bug fix (#85) in library 'raster':
  'raster before skip' and 'raster after skip' did not accept glue anymore.
- new initialization option (#80): 'reset counter on overlays'

version 4.30 (2020/04/28)
- bug fix (#88): 'parskip' and 'noparskip' had side-effects for the box content
                 in combination with 'height fill' and 'parbox=false'
- bug fix (#90) in library 'documentation':
  initialize 'doc description' for every docXXX to be empty
- Internal box counter renamed to remove warnings when using \includeonly
- library 'documentation':
  * major code overhaul to support simultaneous documentation of
    similar commands, environments, keys, path operations (#89).
  * Note that the new code reserves a small additional amount of vertical space
    for documented macros which may result in changed page breaks.
  * Note that documentation heads are now embedded inside a 'raster'
    which requires other customizations for vertical space (if needed)
  * new macros and environments: 'docCommands', 'docEnvironments',
      'docKeys', '\tcbmakedocSubKeys', 'docPathOperations'
  * new options: 'doc index' (#91), 'doc name', 'doc parameter',
      'doc keypath', 'doc sort index', 'doc no index',
      'doc raster command', 'doc raster environment', 'doc raster key',
      'doc raster path', 'doc raster'
  * additional option setting for: '\docAuxCommand', '\docAuxEnvironment',
      '\docAuxKey', '\docValue', '\docColor', '\docCounter', '\docLength'
  * superfluous and undocumented opton 'color frame' removed (#94)
  * '\refAux' and '\refAuxcs' are not longer colored, if colorlinks=false (#95)
- library 'listingsutf8':
  safeguard against compiling with other engines than pdf(la)tex (#92)
- library 'fitting':
  '\tcbfitdim' is described in more detail (#96)
- library 'poster':
  poster width and height caveats described in more detail (#98)

version 4.31 (2020/07/31)
- bug fix (#101): \tcbincludepdf did not work for lualatex
- bug fix (#103): Several tests had a missing \relax
- bug fix (#106): Breakable tcolorbox may overlap with following the text
- bug fix: 'space to' did not result in a stable value
- Internal change: all 'code 2 args' replaced by 'code n args={2}'
- documentation typo corrections (#102)
- library 'documentation':
  * indention of <environment content> changed to \ttfamily (#100)

version 4.32 (2020/09/17)
- documentation typo corrections (#108) and enhancements (#109)
- bug fix (#112): 'index format=doc' caused redefinition of '\_'
    among other errors.
- bug fix: 'valign=scale*' was erroneous.
- enhancement (#110): color stack support for breakable boxes (pdflatex and lualatex)
    to let colors survive a break to the next partial box.
- library 'xparse':
  * new options (#111): 'IfNoValueT', 'IfNoValueF', 'IfValueT', 'IfValueF',
      'IfBooleanT', 'IfBooleanF'

