from .generic import Generic, ShellConfiguration


class Powershell(Generic):
    def app_alias(self, alias_name):
        return 'function ' + alias_name + ' {\n' \
               '    $history = (Get-History -Count 1).CommandLine;\n' \
               '    if (-not [string]::IsNullOrWhiteSpace($history)) {\n' \
               '        $heck = $(theheck $args $history);\n' \
               '        if (-not [string]::IsNullOrWhiteSpace($heck)) {\n' \
               '            if ($heck.StartsWith("echo")) { $heck = $heck.Substring(5); }\n' \
               '            else { iex "$heck"; }\n' \
               '        }\n' \
               '    }\n' \
               '    [Console]::ResetColor() \n' \
               '}\n'

    def and_(self, *commands):
        return u' -and '.join('({0})'.format(c) for c in commands)

    def how_to_configure(self):
        return ShellConfiguration(
            content=u'iex "theheck --alias"',
            path='$profile',
            reload='& $profile',
            can_configure_automatically=False)
