from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

from . import util
# from wiki import encyclopedia

# view for home page


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# view for entry page
# got data but still needs to be formated


def entry_view(request, entry):
    entryContent = util.get_entry(entry)
    if entryContent:
        return render(request, "encyclopedia/entry.html", {"entryTitle": entry.upper, "entryContent": entryContent})
    else:
        return render(request, "encyclopedia/error.html")


def search_view(request):
    entry = request.POST["q"]
    entryContent = util.get_entry(entry)
    if entryContent is not None:
        return render(request, "encyclopedia/entry.html", {"entryTitle": entry.upper, "entryContent": entryContent})
    else:
        return render(request, "encyclopedia/search.html", {"entry": entry, "entries": util.list_entries()})


class NewEntryForm(forms.Form):
    t = forms.CharField(label="Entry")
    c = forms.CharField(widget=forms.Textarea, label="Content")


def new_entry_view(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            entry = form.cleaned_data["t"]
            entryContent = form.cleaned_data["c"]
            old_entry = util.list_entries()
            for e in old_entry:
                if(e == entry):
                    return HttpResponseRedirect(reverse("encyclopedia/error2.html"))
                else:
                    util.save_entry(entry, entryContent)
                    return HttpResponseRedirect(reverse("encyclopedia/entry.html", {"entryTitle": entry.upper, "entryContent": entryContent}))
    else:
        return render(request, "encyclopedia/new_entry.html", {"form": NewEntryForm()})
