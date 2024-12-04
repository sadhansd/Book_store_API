database = {
1: {
   'Title': "Germs : Biological Weapons and America's Secret War",
  'Authors': 'By Miller, Judith, Engelberg, Stephen, and Broad, William J.',
  'Description': "Deadly germs sprayed in shopping malls, bomb-lets spewing anthrax spores over battlefields, tiny vials of plague scattered in Times Square -- these are the poor man's hydrogen bombs, hideous weapons of mass destruction that can be made in a simple laboratory. In this groundbreaking work of investigative journalism, Judith Miller, Stephen Engelberg, and William Broad of The New York Times uncover the truth about biological weapons and show why bio-warfare and bio-terrorism are fast becoming our worst national nightmare.  Among the startling revelations in Germs:   How the CIA secretly built and tested a model of a Soviet-designed germ bomb, alarming some officials who felt the work pushed to the limits of what is permitted by the global treaty banning germ arms. How the Pentagon embarked on a secret effort to make a superbug. Details about the Soviet Union's massive hidden program to produce biological weapons, including new charges that germs were tested on humans. How Moscow's scientists made an untraceable germ that instructs the body to destroy itself. The Pentagon's chaotic efforts to improvise defenses against Iraq's biological weapons during the 1991 Persian Gulf War. How a religious cult in Oregon in the 1980s sickened hundreds of Americans in a bio-terrorism attack that the government played down to avoid panic and copycat strikes. Plans by the U.S. military in the 1960s to attack Cuba with germ weapons.   Germs also shows how a small group of scientists and senior officials persuaded President Bill Clinton to launch a controversial multibillion-dollar program to detect a germ attack on U.S. soil and to aid its victims -- a program that, so far, is struggling to provide real protection.  Based on hundreds of interviews with scientists and senior officials, including President Clinton, as well as on recently declassified documents and on-site reporting from the former Soviet Union's sinister bio-weapons labs, Germs shows us bio-warriors past and present at work at their trade. There is the American scientist who devoted his professional life to perfecting biological weapons, and the Nobel laureate who helped pioneer the new biology of genetically modified germs and is now trying to stop its misuse. We meet former Soviet scientists who made enough plague, smallpox, and anthrax to kill everyone on Earth and whose expertise is now in great demand by terrorists, rogue states, and legitimate research labs alike.  A frightening and unforgettable narrative of cutting-edge science and spycraft, Germs shows us why advances in biology and the spread of germ weapons expertise to such countries as Iran, Iraq, and North Korea could make germs the weapon of the twenty-first century.",
  'Category': ' Technology & Engineering , Military Science',
  'Publisher': 'Simon & Schuster',
  'Price Starting With ($)': 4.99,
  'Publish Date (Month)': 'October',
  'Publish Date (Year)': 2001},
2: {'Title': 'The Genesis of Ethics',
  'Authors': 'By Visotzky, Burton L.',
  'Description': 'none',
  'Category': ' Religion , Ethics',
  'Publisher': 'Crown',
  'Price Starting With ($)': 4.99,
  'Publish Date (Month)': 'September',
  'Publish Date (Year)': 1996}
}

def get_book_from_db(id):
    return database.get(id)