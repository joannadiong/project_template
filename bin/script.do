

********** NOTES **********

  ** Author: [name]
  ** Date: [date]

  ** This do file [describe what it does].
  **
  ** Data are [describe source and content of data file].
  **
  ** The code was checked by [name] on [date]


********** PRELIMINARIES **********

* Install libraries if not yet done so
*ssc install [library], replace

version 16
clear all
clear matrix
drop _all
capture log close

  ** Settings.

set more off
set scheme lean3
pause on

/*
  ** [DEPRECATED] WINDOWS: Enter name of root directory and name of this do file.

local pathname = `""C:\Documents and Settings\Joanna Diong\My Documents\My Stata Files\""'
local dofilename = `""<filename>.do""'

  ** Open a time- and date-stamped log file and copy a time- and date-stamped
  ** do file and data file to the log file directory.

local pathandnameofdofile = `"""' + `pathname' + `dofilename' + `"""'
local pathoflogfilesname = `"""' + `pathname' + "log-files\" + `"""'
local pathofdatafilesname = `"""' + `pathname' + "data\" + `"""'
local pathofgraphfilesname = `"""' + `pathname' + "graphs\" + `"""'
local cdate = "c(current_date)"
local ctime = "c(current_time)"
local ctime = subinstr(`ctime',":","h",1)
local ctime = subinstr("`ctime'",":","m",1)
local logfilename = `"""' + "log " + `cdate' + " " + "`ctime'" + "s.log" + `"""'
local backupdofilename = `"""' + "do " + `cdate' + " " + "`ctime'" + "s.txt" + `"""'
cd `pathoflogfilesname'
*log using `logfilename'
*copy `pathandnameofdofile' `backupdofilename'
cd `pathofdatafilesname'
*/

  ** LINUX: Enter name of root directory and name of this do file.

local projpathname = `""/home/joanna/Dropbox/Projects/<project>/""'
local codepathname = `""src/code/bin/""'
local datarawpathname = `""data/raw/""'
local dataprocpathname = `""data/proc/""'
local dofilename = `""script.do""'

  ** Open a time- and date-stamped log file and copy a time- and date-stamped
  ** do file and data file to the log file directory.

local pathandnameofdofile = `"""' + `projpathname' + `codepathname' + `dofilename' + `"""'
local pathofdatafilesname = `"""' + `projpathname' + `datarawpathname' + `"""'
local pathoflogfilesname = `"""' + `projpathname' + `dataprocpathname' + `"""'
local pathofgraphfilesname = `"""' + `projpathname' + `dataprocpathname' + `"""'
local cdate = "c(current_date)"
local ctime = "c(current_time)"
local ctime = subinstr(`ctime',":","h",1)
local ctime = subinstr("`ctime'",":","m",1)
local logfilename = `"""' + "log " + `cdate' + " " + "`ctime'" + "s.log" + `"""'
local backupdofilename = `"""' + "do " + `cdate' + " " + "`ctime'" + "s.txt" + `"""'
cd `pathoflogfilesname'
*log using `logfilename'
*copy `pathandnameofdofile' `backupdofilename'
cd `pathofdatafilesname'


********** IMPORT DATA AND CLEAN **********

cd `pathofdatafilesname'
import excel "<filename>.xlsx", sheet("Sheet1") firstrow clear

drop in 1

quietly {
rename Studyname studyname
rename Comparison comparison
rename Outcome outcome
}

label variable studyname "Study name"


********** RUN ANALYSIS **********

summarize var1-var5

label define femalemale 0 "Male" 1 "Female"
label values sex femalemale

  ** Describe age and sex by group.

foreach vname of varlist age {
display in green _n _n "ANALYSIS OF: " "`vname'"
table group, contents(mean `vname' sd `vname' count `vname' min `vname' max `vname') row
}
tabulate sex group, column exact

  ** Summarise variables by group, compare EXP and CON groups after adjusting for shank length.

foreach vname of varlist var1 var2 var3 {
display _n _n in green "ANALYSIS OF: " "`vname'"
local tableoptions row center format(%12.5fc)
if "`vname'" == "lnalphag" local tableoptions row center format(%12.3fc)
table group if group == "CON" | group == "EXP", ///
    contents(mean `vname' sd `vname' count `vname' min `vname' max `vname') `tableoptions'
regress `vname' con ls if group == "CON" | group == "EXP"
predict yhat, xb
tabstat yhat, statistics(mean) by(group)
drop yhat

********** GRAPH DATA **********

cd `pathofgraphfilesname'
hist var2
graph export "Example graph.tif", replace

notes: best variable name convention: varname_group_subjectid

foreach lname of varlist * {
if substr("`lname'",1,5) == "alpha" & substr("`lname'",7,3) == "nor" {
  local suffix = substr("`lname'",6,.)
  local aa : display `"`aa'"' `"(line alpha"' `"`suffix'"' `" "' `"force"' `"`suffix'"' `", lpattern(solid) lcolor(blue)) "'
}
if substr("`lname'",1,5) == "alpha" & substr("`lname'",7,3) == "sci" {
  local suffix = substr("`lname'",6,.)
  local bb : display `"`bb'"' `"(line alpha"' `"`suffix'"' `" "' `"force"' `"`suffix'"' `", lpattern(solid) lcolor(red)) "'
}
}

twoway `aa' `bb',                                           ///
xtitle("Title in X (units)") xlabel(0(100)300) xsize(3)   ///
ytitle("Title in Y (units)") ylabel(0(10)30) ysize(2)     ///
legend(ring(0) position(2) order(1 "Control" 30 "SCI") colfirst notextfirst) text(100 -10 "a") scale(1.25)
*quietly graph export "aabb.tif", width(900) height(600) replace
*graph drop Graph
graph save aabb, replace

twoway `cc' `dd',                                           ///
xtitle("Title in X (units)") xlabel(0(100)300) xsize(2)   ///
ytitle("Title in Y (units)") ylabel(0(10)30) ysize(2)     ///
legend(ring(0) position(2) order(1 "Control" 30 "SCI") colfirst notextfirst) text(100 -10 "b") scale(1.25)
*quietly graph export "ccdd.tif", width(900) height(600) replace
*graph drop Graph
graph save ccdd, replace
graph combine aabb.gph ccdd.gph, col(1) xsize(3) ysize(4) //Edit xsize and ysize in twoway options
graph export aabbccdd.tif, width(900) height(1200) replace


********** END **********

*log close
exit
