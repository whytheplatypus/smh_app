from collections import defaultdict
from importlib import import_module

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Organization, ResourceGrant


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "org/dashboard.html"

    def get_context_data(self, **kwargs):
        """Add the user's Organizations to the context."""
        # All of the Organizations that the request.user is a part of
        organizations = self.request.user.organization_set.all()

        kwargs.setdefault('organizations', organizations)
        return super().get_context_data(**kwargs)


class CreateOrganizationView(LoginRequiredMixin, CreateView):
    model = Organization
    fields = ['name', 'users']
    template_name = 'org/organization.html'
    success_url = reverse_lazy('org:dashboard')

    def form_valid(self, form):
        """Override this method to also associate the creator with the new Organization."""
        # Now that the form has passed validation, save the object, then add
        # the request.user to its users.
        response = super().form_valid(form)
        form.instance.users.add(self.request.user)
        return response


class UpdateOrganizationView(LoginRequiredMixin, UpdateView):
    model = Organization
    fields = ['name', 'users']
    template_name = 'org/organization.html'
    success_url = reverse_lazy('org:dashboard')

    def get_queryset(self):
        """A user may only edit Organizations that they are associated with."""
        qs = super().get_queryset()
        return qs.filter(users=self.request.user)


class DeleteOrganizationView(LoginRequiredMixin, DeleteView):
    model = Organization
    success_url = reverse_lazy('organization-list')
    template_name = 'org/organization_confirm_delete.html'
    success_url = reverse_lazy('org:dashboard')

    def get_queryset(self):
        """A user may only delete Organizations that they are associated with."""
        qs = super().get_queryset()
        return qs.filter(users=self.request.user)
