# wikipit
A Command Line Tool to Search Wikipedia in the terminal.

 - [Installation](#installation)
 - [Usage](#usage)
   - [Examples](#examples)
   - [Flags](#flags)
   - [Output](#output)
 - [Support Development](#support-development)

 ## Installation

`$ pip install wikipit`

## Usage

Syntax: `$ wikipit <query> [-flags]`

Quotes are required for multi-word queries.

### Examples

`$ wikit wikipedia`

`$ wikit "Miguel Cabrera"`

`$ wikit linux -b`

`$ wikit "Miguel Cabrera" -l 8`

### Flags

| Flag | Description |
| ---- | ----------- |
| `--l num` | Set line wrap length to `num` |
| `-b` | Open full Wikipedia article in default browser |
| `--all`<br>`-a` | Print all sections of the article (the full page). Recommended to pipe into a reader e.g. `less` |

### Output

The output will be the paragraphs of the wikipedia article before the table of contents.
Line length is neatly wrapped based on your terminal's window size, For example:

```
$ wikipit "Miguel Cabrera"
 José Miguel Cabrera Torres (born April 18, 1983), commonly known as Miguel 
 Cabrera and nicknamed "Miggy", is a Venezuelan professional baseball player. 
 He is the first baseman for the Detroit Tigers of Major League Baseball (MLB).
 Since his debut in 2003 he has been a two-time American League (AL) Most 
 Valuable Player (MVP) award winner, a four-time AL batting champion, and an 
 11-time MLB All-Star. He has played at first and third base for most of his 
 major league career, but primarily played left and right field before 2006. He 
 claimed the 17th MLB Triple Crown in 2012, the first to do so in 45 seasons. 
 In Venezuelan Winter League, Liga de Beisbol Profesional de Venezuela, Cabrera was
 signed by Tigres de Aragua at 16 years old. He batted his first hit in 
```

### Support development

If you liked this, donate to the cause.

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.me/carrasquel)
